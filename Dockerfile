# Образ для Django-приложения TechnoService
FROM python:3.12-slim

# Не создавать .pyc и буферизовать вывод
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Рабочая директория в контейнере
WORKDIR /app

# Установка системных зависимостей (для psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Копируем и устанавливаем зависимости Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код проекта
COPY . .

# Папки для статики и медиа (создаются при старте)
RUN mkdir -p /app/staticfiles /app/media

# Собираем статику при сборке (БД не нужна, используется SQLite по умолчанию)
RUN python manage.py collectstatic --noinput --clear 2>/dev/null || true

# Открываем порт
EXPOSE 8000

# Скрипт запуска (миграции + gunicorn)
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
