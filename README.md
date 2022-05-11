# Куда пойти — Москва глазами Артёма
[Посмотреть демоверсию сайта](https://konakovmark.pythonanywhere.com/)
## Как запустить

- Скачайте код
- Установите зависимости `pip install -r requirements.txt`
- Создайте базу данных проекта `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

## Переменные окружения

Создайте файл `.env` рядом с `manage.py`

Доступны 3 переменные:
- `DEBUG` — True, если необходимо вывести отладочную информацию.
- `SECRET_KEY` — секретный ключ проекта.
- `ALLOWED_HOSTS` — см [документацию](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
