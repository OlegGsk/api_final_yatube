# REST API для проекта Yatube

## Yatube — это платформа для блогов. Предполагает возможность создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.

## Через этот программный интерфейс смогут работать не только браузер ,но и мобильное приложение или чат-бот; данные через этот API можно будет передавать и на фронтенд.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://git@github.com:OlegGsk/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## endpoints:

### Публикации

```
http://127.0.0.1:8000/api/v1/posts/  - методы GET, POST. Получение всех публикаций, и создание новой публикации
```
Request POST:
```
payload
{
"text": "string",
"image": "string",
"group": 0
}
```
Response:
```
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```

```
http://127.0.0.1:8000/api/v1/posts/{id} -методы GET, PUT, PATCH, DELETE. Получение,обновление и удаление
отдельной публикации
```
Request PUT:
```
payload
{
"text": "string",
"image": "string",
"group": 0
}
```
Response
```
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```
Request PATCH:
```
payload
{
"text": "string1",
"image": "string1"
}
```
Response:
```
{
"id": 0,
"author": "string",
"text": "string1",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string1",
"group": 0
}
```

### Комментарии

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/  - методы GET, POST.Получение всех комментариев и
создание нового
```

Request POST:
```
payload
{
"text": "string"
}
```
Response:
```
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id} -методы GET, PUT, PATCH, DELETE. Получение, обновление и
удаление отдельного комментария
```
Request PATCH:
```
payload
{
"text": "string2"
}
```
Response:
```
{
"id": 0,
"author": "string",
"text": "string2",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```

### Сообщества

```
http://127.0.0.1:8000/api/v1/groups/ - метод GET. Получение списка сообществ
```
```
http://127.0.0.1:8000/api/v1/groups/{id} - метод Get. Информация о отдельном сообществе
```

### Подписка

```
http://127.0.0.1:8000/api/v1/follow/ - метод GET. Возвращает все подписки пользователя
```
```
http://127.0.0.1:8000/api/v1/follow/ - метод POST. Подписка пользователя от имени которого сделан запрос
на пользователя переданного в теле запроса
```
Request POST:
```
payload
{
"following": "author_name"
}
```
Response:
```
{
"user": "user_name",
"following": "author_name"
}
```

### JWT-TOKEN

```
http://127.0.0.1:8000/api/v1/jwt/create/ - метод POST. Получить jwt-token
```
Request POST:
```
payload
{
"username": "string",
"password": "string"
}
```
Response:
```
{
"refresh": "string",
"access": "string"
}
```
```
http://127.0.0.1:8000/api/v1/jwt/refresh/ - метод POST. Обновить jwt-token
```
Request POST:
```
payload
{
"refresh": "string"
}
```
Response:
```
{
"access": "string"
}
```
```
http://127.0.0.1:8000/api/v1/jwt/verify/ - метод POST. Проверить jwt-token
```

