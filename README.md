# Rassilka API

Hello to my test project!
This is a test Django/DRF project using Celery

## REQUIREMENTS

You can find in file **requirements.txt**


## INSTALLATION

1) change **.env.env** global variables such as DB, API, etc

2) In your shell:

`docker-compose build`

`docker-compose run rassilka sh -c "python manage.py makemigratons"`

`docker-compose run rassilka sh -c "python manage.py createsuperuser"`

Set your login, email, password

`docker-compose run rassilka sh -c "python manage.py makemigrations"`

Final step

`docker-compose up --build`


## FIRST RUN

After building docker in your browser open http://127.0.0.1:8000

After login you will see admin panel

### API

There are following API endpoints:

Get the JWT tokens at http://127.0.0.1:8000/api/v1/token

Refresh at http://127.0.0.1:8000/api/v1/token/refresh/

To add/edit/delete:
- campaigns use http://127.0.0.1:8000/api/v1/campaigns/
- customers use http://127.0.0.1:8000/api/v1/customers/

For statistics:
- customers use http://127.0.0.1:8000/api/v1/stats/


### Swagger UI

You can learn about API at https://127.0.0.1/docs/

