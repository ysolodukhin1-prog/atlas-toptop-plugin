# Вход в GALACTICA через встроенный браузер Codex

Этот сценарий выполняет Codex по просьбе пользователя установить/подключить плагин и использовать встроенный браузер. Пользователь вводит пароль только на обычной странице TREND. Python, SSH и ручной перенос файлов не нужны.

## Как устроен возврат

1. Локальный Codex CLI запускается с `--no-browser` и HTTPS callback GALACTICA.
2. Помощник открывает выданный authorization URL в браузере `iab` и сохраняет работающий процесс.
3. TREND использует текущую личную сессию или показывает штатную страницу входа.
4. Браузер возвращается на `https://83.222.17.242/galactica-mcp/oauth/codex-callback/<id>#…`. Это служебная страница ожидания. Наличие этой страницы ещё не подтверждает подключение.
5. Помощник сверяет адрес и `state`, преобразует фрагмент в query только в памяти и передаёт адрес в stdin ожидающего CLI. Сам CLI проверяет OAuth и обменивает код с PKCE.
6. После завершения CLI и успешного `whoami` помощник открывает GALACTICA и TREND в двух вкладках.

Браузер не обращается к `127.0.0.1`. Код находится во фрагменте адреса, который не отправляется HTTP-серверу и в access log. Подготовленный для stdin адрес с query **нельзя открывать в браузере или отправлять HTTP-запросом**.

## Запуск: обязательные условия

- Сверь `codex mcp login --help`: нужны `--no-browser` и `--oauth-client-registration`.
- Найди установленный Codex CLI штатным способом, например `(Get-Command codex).Source` в PowerShell. Не используй путь другого пользователя.
- Нужны живой дочерний процесс с stdin pipe и поддерживаемый браузерный инструмент Codex. В Windows проверен запуск из постоянного Node REPL, уже доступного в среде Codex. Пользователю не предлагается устанавливать Node или Python.
- Не запускай вход через одноразовый shell, закрывающий stdin. Не используй Windows PTY для длинного callback: в проверке такой ввод дал `OAuth callback URL is missing state`.
- Не запускай параллельные входы. Сохраняй ссылку на процесс, authorization URL и ожидаемый redirect URI только в памяти до завершения или отмены.

## Пример для постоянного Node REPL

Это пример проверяемого кода оркестрации, а не команда для пользователя. Сначала прочитай возможности инструментов текущего Codex. Управляй браузером только через поддерживаемый браузерный инструмент, не через HTTP-запросы, cookie-файлы или собственный browser automation.

`codexExecutable` ниже — фактически найденный путь к CLI на компьютере пользователя.

```javascript
var childProcess = await import('node:child_process');
var login = childProcess.spawn(codexExecutable, [
  '-c', 'mcp_servers.galactica_toptop_client.url="https://83.222.17.242/galactica-mcp/mcp"',
  '-c', 'mcp_servers.galactica_toptop_client.oauth.callback_url="https://83.222.17.242/galactica-mcp/oauth/codex-callback"',
  'mcp', 'login', 'galactica_toptop_client',
  '--no-browser', '--oauth-client-registration', 'dcr'
], { stdio: ['pipe', 'pipe', 'pipe'], windowsHide: true });
var loginOutput = '';
var loginDiagnostic = '';
login.stdout.on('data', chunk => { loginOutput += chunk.toString(); });
login.stderr.on('data', chunk => { loginDiagnostic += chunk.toString(); });
var loginFinished = new Promise((resolve, reject) => {
  login.once('error', reject);
  login.once('close', resolve);
});
```

Следующим коротким вызовом REPL получи свежий authorization URL из stdout. Если вывода пока нет, проверь снова после другой полезной работы; не держи один вызов инструмента на несколько минут. Если процесс завершился, покажи очищенную от URL диагностику и начни новую попытку только после устранения причины.

```javascript
var authorizationUrl = loginOutput.match(
  /https:\/\/83\.222\.17\.242\/galactica-mcp\/oauth\/authorize\?\S+/
)?.[0];
if (!authorizationUrl) throw new Error('Authorization URL пока не получен');
var authorization = new URL(authorizationUrl);
var expectedRedirect = authorization.searchParams.get('redirect_uri');
var expectedState = authorization.searchParams.get('state');
if (!expectedRedirect || !expectedState) throw new Error('Неполный OAuth-запрос');
var redirect = new URL(expectedRedirect);
if (redirect.origin !== 'https://83.222.17.242' ||
    !/^\/galactica-mcp\/oauth\/codex-callback(?:\/[A-Za-z0-9_-]{8,128})?$/.test(redirect.pathname) ||
    redirect.search || redirect.hash || redirect.username || redirect.password) {
  throw new Error('CLI не использует ожидаемую HTTPS-страницу возврата');
}
```

Открой `authorizationUrl` во встроенном браузере (`iab`, видимая вкладка), используя актуальный API браузерного инструмента. Если пользователь должен ввести пароль, оставь вкладку и процесс доступными, дождись его сообщения. Не нажимай отмену, не закрывай процесс и не создавай новую попытку, пока человек входит.

После возврата получи **текущий URL именно этой вкладки** поддерживаемым браузерным инструментом. Держи его в памяти как `browserCallbackUrl`; не выводи его в ответ пользователю, не записывай в файл, историю shell или журнал. Не снимай скриншот с одноразовым кодом в адресной строке. Никогда не используй URL из старого сообщения, скриншота или другой попытки.

```javascript
var returned = new URL(browserCallbackUrl);
var response = new URLSearchParams(returned.hash.slice(1));
var keys = [...response.keys()];
if (returned.origin + returned.pathname !== expectedRedirect || returned.search ||
    returned.username || returned.password ||
    keys.length !== 2 || new Set(keys).size !== 2 ||
    !response.get('code') || response.get('state') !== expectedState ||
    !keys.every(key => key === 'code' || key === 'state')) {
  throw new Error('Результат входа не соответствует текущему запросу');
}
if (login.exitCode !== null || login.killed || !login.stdin.writable) {
  throw new Error('Ожидающий процесс входа уже завершился; нужна свежая попытка');
}
returned.search = returned.hash.slice(1);
returned.hash = '';
login.stdin.end(returned.href + '\n');
// Жди завершения короткими вызовами, не обрывая процесс по таймауту инструмента.
```

Дождись `loginFinished` или проверь `login.exitCode`; успех — только код `0`. Не печатай необработанную диагностику: она может содержать адреса. Очисти из памяти callback и накопленный вывод после завершения. Токены сохраняет сам Codex штатным механизмом — не читай и не копируй его файлы учётных данных.

## После входа

Вызови настоящий `whoami` через установленное MCP и сверяй личность. Если текущий чат продолжает использовать старое подключение, открой новый чат либо используй штатное переподключение MCP. Успех CLI означает завершение OAuth, но не обновление всех уже работающих чатов.

Проверь `get_context({})` и `trend_list_sources({})`. Затем замени вкладку входа на `https://83.222.17.242/galactica/` и открой рядом `https://83.222.17.242/react/?client=toptop&dashboard=home&marketplace=total` в том же `iab`. Проверь рабочие интерфейсы и сохрани обе вкладки для пользователя. Не меняй OAuth redirect URI на `/galactica/`: обмен кодом должен закончиться до открытия рабочего интерфейса.

Если нужных возможностей в текущем клиенте нет, назови отсутствующую возможность. Не обещай работу во встроенном браузере для любой версии Codex. Claude Code использует свой штатный вход `/mcp`; этот способ управления вкладками относится к Codex desktop.

## Проверено 28.09.2026

На Windows, Codex CLI `0.158.0-alpha.2.1`: реальный вход в `iab` с существующей сессией TREND → HTTPS fragment callback → stdin pipe → CLI exit 0 → `whoami` настоящим MCP-клиентом Codex под текущим пользователем → чтение контекста и каталог источников. Пароли, cookie и файлы токенов не читались. При отсутствии браузерной сессии сервер направляет на штатный TREND `/login`. Это не гарантия совместимости со всеми версиями клиента.

Справка о настройках callback: [официальная документация Codex](https://learn.chatgpt.com/docs/config-file/config-reference). Поддержку manual input проверяй справкой установленного CLI.
