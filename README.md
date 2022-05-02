# API_quiz
Service for send requests to quiz by API

## Описание.

Проект **API_quiz** сохраняет в базе данных англоязычные вопросы для викторин, полученные с публичного [API сервиса](https://jservice.io/api/random?count=1).

## Установка на локальном компьютере.
Эти инструкции помогут вам создать копию проекта и запустить ее на локальном компьютере для целей разработки и тестирования.

### Установка Docker.
Установите Docker, используя инструкции с официального сайта:
- для [Windows и MacOS](https://www.docker.com/products/docker-desktop)
- для [Linux](https://docs.docker.com/engine/install/ubuntu/). Отдельно потребуется установть [Docker Compose](https://docs.docker.com/compose/install/)

### Запуск проекта.
- Склонируйте этот репозиторий в текущую папку `git clone https://github.com/Elegantovich/API_quiz/`
- Создайте файл `.env` командой `touch .env` и добавьте в него переменные окружения для работы с базой данных:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432 
DJANGO_KEY='your_key'
```
Запустите docker-compose командой:
```
docker-compose up -d --build
```
Накатите миграции:
```
docker-compose exec web python manage.py migrate
```
Отправьте POST запрос по адресу http://127.0.0.1:8000/api/question/ с телом == кол-ву запросов к вышеуказанному [API сервису](https://jservice.io/api/random?count=1):
```
{"questions_num": int}
```
В ответ придет предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

### Авторы

[Хачатрян Максим](https://github.com/Elegantovich)<br>
