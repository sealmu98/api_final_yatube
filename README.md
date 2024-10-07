# API для Yatube
**RU**
## Описание

**Yatube** - это социальная сеть, в которой пользователи могут создавать посты, комментировать их, подписываться на других пользователей и создавать группы. Этот проект представляет собой RESTful API, который позволяет взаимодействовать с социальной сетью через HTTP-запросы.

## Что было сделано

**В этом проекте я реализовал следующий функционал:**
* Разработал RESTful API для социальной сети Yatube с использованием Django и Django REST framework.
* Создал модели для постов, комментариев, групп и подписок.
* Реализовал вьюсеты для обработки запросов к API.
* Настроил аутентификацию и авторизацию с использованием JWT-токенов.
* Добавил пермишены для ограничения доступа к API для неаутентифицированных пользователей.
* Развернул проект на локальной машине с использованием виртуального окружения и SQLite базы данных.


## Стек технологий проекта
![Python](https://img.shields.io/badge/-Python-black?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/-Django-black?style=for-the-badge&logo=Django)
![DRF](https://img.shields.io/badge/-Django_REST_Framework-black?style=for-the-badge&logo=DRF)
![SQLite](https://img.shields.io/badge/-SQLite-black?style=for-the-badge&logo=SQLite)
![JWT](https://img.shields.io/badge/-JWT-black?style=for-the-badge&logo=JWT)
![Linux](https://img.shields.io/badge/-Linux-black?style=for-the-badge&logo=Linux)
![Postman](https://img.shields.io/badge/-Postman-black?style=for-the-badge&logo=postman)


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:your_username_in_github/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd yatube_api
```

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов к API
**Посты**
* Получение списка постов: ```GET /api/v1/posts/```
* Создание нового поста: ```POST /api/v1/posts/```
* Получение информации о посте: ```GET /api/v1/posts/{id}/```
* Обновление поста: ```PUT /api/v1/posts/{id}/```
* Удаление поста: ```DELETE /api/v1/posts/{id}/```

**Комментарии**
* Получение списка комментариев к посту: ```GET /api/v1/posts/{id}/comments/```
* Создание нового комментария к посту: ```POST /api/v1/posts/{id}/comments/```
* Получение информации о комментарии: ```GET /api/v1/posts/{id}/comments/{comment_id}/```
* Обновление комментария: ```PUT /api/v1/posts/{id}/comments/{comment_id}/```
* Удаление комментария: ```DELETE /api/v1/posts/{id}/comments/{comment_id}/```

**Группы**
* Получение списка групп: ```GET /api/v1/groups/```
* Создание новой группы: ```POST /api/v1/groups/```
* Получение информации о группе: ```GET /api/v1/groups/{id}/```
* Обновление группы: ```PUT /api/v1/groups/{id}/```
* Удаление группы: ```DELETE /api/v1/groups/{id}/```

**Подписки**
* Получение списка подписок: ```GET /api/v1/follow/```
* Создание новой подписки: ```POST /api/v1/follow/```
* Удаление подписки: ```DELETE /api/v1/follow/{id}/```

**Аутентификация**
* Получение токена для аутентификации: ```POST /api/v1/jwt/create/```
* Обновление токена для аутентификации: ```POST /api/v1/jwt/refresh/```
* Проверка токена для аутентификации: ```POST /api/v1/jwt/verify/```
* Аутентификация с помощью токена: ```POST /api/v1/api-token-auth/```

**Эти примеры демонстрируют основные возможности API для Yatube. Для более подробной информации о запросах и ответах можно обратиться к документации API.**
