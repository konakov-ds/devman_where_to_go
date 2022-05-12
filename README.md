# Куда пойти — интересные места Москвы
[Посмотреть демоверсию сайта](https://konakovmark.pythonanywhere.com/)
## Как запустить

- Скачайте код
- Установите зависимости:
  ```
  pip install -r requirements.txt
  ```
- Создайте базу данных проекта:
  ```
  python manage.py migrate
  ```
- Запустите сервер командой:
  ```
  python manage.py runserver
  ```

## Переменные окружения

Создайте файл `.env` рядом с `manage.py`

Доступны 3 переменные:
- `DEBUG` — True, если необходимо вывести отладочную информацию.
- `SECRET_KEY` — секретный ключ проекта.
- `ALLOWED_HOSTS` — см [документацию](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).

## Добавление мест

Для загрузки локаций можно воспользоваться командой:
```
python3 manage.py load_place <link>`.
```

Файл для загрузки локации должен быть выполнен по [образцу](https://github.com/devmanorg/where-to-go-places/blob/master/places/%D0%92%D0%BE%D1%80%D0%BE%D0%B1%D1%8C%D1%91%D0%B2%D1%8B%20%D0%B3%D0%BE%D1%80%D1%8B.json).
