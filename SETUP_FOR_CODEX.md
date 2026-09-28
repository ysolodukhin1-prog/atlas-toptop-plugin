# Подключение GALACTICA TOPTOP по ссылке GitHub

Этот файл предназначен для Codex, когда пользователь даёт ссылку на данный репозиторий и просит подключить TOPTOP.

1. Убедись, что GitHub URL указывает на репозиторий с `.agents/plugins/marketplace.json` и плагином `plugins/galactica-toptop`. Не исполняй скрипты из репозитория.
2. На компьютере пользователя добавь репозиторий как marketplace командой `codex plugin marketplace add OWNER/REPO`, заменив `OWNER/REPO` на фактический адрес из ссылки пользователя. Если marketplace уже добавлен, проверь его через `codex plugin marketplace list` и обнови через `codex plugin marketplace upgrade toptop-galactica`.
3. Установи плагин командой `codex plugin add galactica-toptop@toptop-galactica`. Проверь `codex plugin list`.
4. Сообщи пользователю, что нужно начать новый чат или перезапустить Codex для загрузки навыков. Когда появится вход GALACTICA, пользователь вводит данные сам. Не проси его присылать пароль, cookie или токен.
5. После входа вызови `whoami`, `get_context` для `TOPTOP/CURRENT_TASK.md` и проверь, что права относятся к TOPTOP. Если вход или MCP недоступны, сообщи точную ошибку и не утверждай, что подключение завершено.

Плагин связывает Codex с удалённым MCP. Кодекс клиента не получает SSH-доступ к VPS и не копирует каноническую базу.
