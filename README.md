Бэкенд-система для проверки IMEI устройств, которая интегрирована с Telegram-ботом и предоставляет API для внешних запросов.

Для запуска необходимо: 

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/trub24/imei_backend.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env source venv/Scripts/activate 
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в нужную директорию и выполнить миграции:

```
python manage.py migrate
```

Запустить проект:
```
python manage.py runserver
```

Пример запроса:

Метод: POST /api/check-imei
```
  Параметры запроса:
    imei (строка, обязательный) — IMEI устройства.
    token (строка, обязательный) — токен авторизации.

Ответ:
JSON с информацией о IMEI.
```
