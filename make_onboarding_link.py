"""Admin helper: print the Codex onboarding link after the GitHub repo is live."""

from __future__ import annotations

import argparse
from urllib.parse import quote, urlsplit


def link(repo_url: str) -> str:
    url = urlsplit(repo_url.rstrip("/"))
    if (url.scheme != "https" or url.hostname != "github.com" or
            url.username or url.password or url.query or url.fragment or
            len([part for part in url.path.split("/") if part]) != 2):
        raise ValueError("Expected https://github.com/OWNER/REPO")
    repo = repo_url.rstrip("/")
    prompt = (
        f"Подключи мой Codex к TOPTOP GALACTICA из {repo}. "
        "Прочитай SETUP_FOR_CODEX.md в корне репозитория и выполни настройку плагина. "
        "Проверь установку и доступ через whoami и get_context. "
        "Если нужны подтверждение установки или вход, попроси меня выполнить их."
    )
    return "codex://new?prompt=" + quote(prompt, safe="")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo_url", help="Published GitHub URL, for example https://github.com/OWNER/REPO")
    args = parser.parse_args()
    print(link(args.repo_url))


if __name__ == "__main__":
    main()
