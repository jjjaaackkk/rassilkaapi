# Rassilka API

Hello to my test project!
This is a Django/DRF project using Celery

## REQUIREMENTS

You can find in file **requirements.txt**


## INSTALLATION

1) update DB credentials in **.env.env** file

2) In your shell:

`docker-compose build`

`docker-compose run rassilka sh -c "python manage.py migrate"`

`docker-compose run rassilka sh -c "python manage.py createsuperuser"`

Set your login, email, password

3) build docker

`docker-compose up --build`

4) Add your API KEY in http://127.0.0.1:8000/account/settings


## FIRST STEPS

After building docker in your browser open http://127.0.0.1:8000

After login you will see admin panel

### API

There are the following API endpoints:

Get the JWT tokens at http://127.0.0.1:8000/api/v1/token

Refresh at http://127.0.0.1:8000/api/v1/token/refresh/

To add/edit/delete

for campaigns use
- http://127.0.0.1:8000/api/v1/campaigns/
- http://127.0.0.1:8000/api/v1/campaigns/{ID}
   
for customers use:
- http://127.0.0.1:8000/api/v1/customers/
- http://127.0.0.1:8000/api/v1/customers/{ID}
   
for messages use:
- http://127.0.0.1:8000/api/v1/messages/{ID}

for statistics use: 
- http://127.0.0.1:8000/api/v1/stats/
- http://127.0.0.1:8000/api/v1/stats/{ID}


### Swagger UI

You can learn more about API using https://127.0.0.1/docs/

## TODO

- Fix 3rd party API problems
- Fix bugs
- Maybe add k8s