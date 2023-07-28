# Rassilka API

Тестовый проект на Django/DRF с использованием Celery

## Установка

1) Заполнить конфигурационный файл **.env.env** file

2) В cmd/batch прописать следующие команды:

`docker-compose build`

`docker-compose run rassilka sh -c "python manage.py migrate"`

`docker-compose run rassilka sh -c "python manage.py createsuperuser"`

По запросу установть login, email и пароль администратора Django

3) Финальная команда для запуска Docker

`docker-compose up --build`

4) В разделе НАСТРОЙКИ прописать API KEY сервиса http://127.0.0.1:8000/account/settings


### Работа с API

Для начала работы с API приложения необходимо получить **ACCESS** и **REFRESH** токены на соответсвенных ссылках:

http://127.0.0.1:8000/api/v1/token
http://127.0.0.1:8000/api/v1/token/refresh/

После получения токенов можно работать непосредственно с API по следующим ссылкам

#### Работа с рассылками

- Получить список всех рассылок: http://127.0.0.1:8000/api/v1/campaigns
- Создать/Получить/Изменить/Удалить рассылку: campaigns use http://127.0.0.1:8000/api/v1/campaigns/{ID}

#### Работа с клиентами

- Получить список всех рассылок: http://127.0.0.1:8000/api/v1/customers
- Создать/Получить/Изменить/Удалить рассылку: campaigns use http://127.0.0.1:8000/api/v1/campaigns/{ID}

#### Удаление сообщений

http://127.0.0.1:8000/api/v1/messages/{ID}


#### Подробная документация по API доступна Swagger UI

https://127.0.0.1/docs/


### Работа с WebUI

По адресу http://127.0.0.1:8000/ доступна административная панель

#### Рассылки

http://127.0.0.1:8000/account/campaigns

Здесь можно Просмотреть/Создать/Изменить/Удалить рассылки

#### Клиенты

http://127.0.0.1:8000/account/customers

Здесь можно Просмотреть/Создать/Изменить/Удалить клиентов

#### Сообщения

http://127.0.0.1:8000/account/messages

Здесь можно удалить сообщения

#### Сообщения

http://127.0.0.1:8000/account/settings

Здесь можно задать API KEY


