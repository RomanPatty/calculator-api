# API Calculator

Учебный API-калькулятор на Python с использованием FastAPI.

Приложение выполняет основные арифметические операции через HTTP-запросы и запускается в Docker-контейнере.

## Возможности

Реализованы следующие операции:

- сложение;
- вычитание;
- умножение;
- деление;
- возведение в степень.

Также приложение предоставляет информацию о текущей версии сборки.

## Основные технологии

- Python 3.13;
- FastAPI;
- Uvicorn;
- Docker;
- Git;
- GitHub;
- GitHub Actions;
- Semgrep;
- Trivy;
- Syft;
- Grype;
- Gitleaks;
- Checkov.

## Локальный запуск

Установить зависимости:

```bash
pip install -r requirements.txt
```

Запустить приложение:

```bash
python -m uvicorn main:app --reload
```

После запуска Swagger UI доступен по адресу:

```text
http://127.0.0.1:8000/docs
```

## Docker

Сборка образа:

```bash
docker build -t calculator-api .
```

Запуск контейнера:

```bash
docker run --name calculator-container -p 8000:8000 calculator-api
```

Dockerfile самостоятельно:

- использует базовый образ `python:3.13-slim`;
- получает версию приложения через `APP_VERSION`;
- создаёт рабочую директорию `/app`;
- копирует `requirements.txt`;
- устанавливает Python-зависимости;
- копирует `main.py`;
- запускает приложение через Uvicorn на порту 8000.

## CI Pipeline

CI-пайплайн описан в файле:

```text
.github/workflows/ci.yml
```

После замечания преподавателя пайплайн был перенесён с GitHub-hosted Ubuntu runner на Windows self-hosted runner.

Текущая схема:

```text
push в main
→ GitHub Actions
→ Windows self-hosted runner
→ Docker Desktop
→ docker build по Dockerfile
→ автоматические проверки безопасности
```

Для основного job используется:

```yaml
runs-on: [self-hosted, Windows, X64]
```

GitHub передаёт задание на зарегистрированный Windows-компьютер. На нём должен быть запущен self-hosted runner и Docker Desktop.

Сборка приложения выполняется непосредственно командой `docker build`, а не отдельной установкой Python и зависимостей внутри runner.

## Версионирование

При сборке в Docker передаётся номер версии:

```text
1.0.<github.run_number>
```

Например:

```text
1.0.5
1.0.6
1.0.7
```

Версия передаётся в Docker через `APP_VERSION`.

## Автоматические проверки безопасности

После сборки Docker-образа pipeline запускает несколько инструментов безопасности.

### Semgrep

Проверяет исходный код и конфигурационные файлы на потенциально небезопасные конструкции.

### Trivy

Проверяет Docker-образ, системные пакеты и Python-зависимости на известные уязвимости.

### Syft

Формирует SBOM — список компонентов, библиотек, системных пакетов и их версий, входящих в Docker-образ.

SBOM формируется в формате SPDX JSON.

### Grype

Проверяет компоненты из SBOM на известные уязвимости.

### Gitleaks

Проверяет Git-репозиторий на случайно опубликованные секреты:

- пароли;
- токены;
- API-ключи;
- приватные ключи;
- другие чувствительные данные.

### Checkov

Проверяет Dockerfile и CI-конфигурацию на небезопасные настройки.

## Self-hosted runner

Self-hosted runner установлен на Windows.

Для запуска runner используется:

```powershell
C:\actions-runner\run.cmd
```

После запуска должно появиться сообщение:

```text
Listening for Jobs
```

Важно:

- Docker Desktop должен быть запущен;
- окно runner должно оставаться открытым;
- если runner выключен или имеет статус Offline, GitHub Actions будет ждать доступную машину;
- Docker Desktop используется в режиме Linux containers, поэтому внутри Docker применяются Linux-образы, несмотря на то что сам runner работает под Windows.

## Результат

В проекте реализована следующая цепочка:

```text
разработка API
→ Docker
→ GitHub
→ CI
→ Windows self-hosted runner
→ автоматическая сборка
→ автоматические проверки безопасности
→ анализ найденных проблем
```

Подробный анализ результатов проверок находится в файле:

```text
SECURITY_ANALYSIS.md
```
