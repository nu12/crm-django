# Getting started with Django

This is the code from the course "Getting Started With Django", found on YouTube.

* [Course video](https://www.youtube.com/watch?v=fOukA4Qh9QA)
* [Course repository](https://github.com/justdjango/getting-started-with-django)

## Development

Create `.env` file. Use `.template.env` as a template.

```shell
$ docker run --name djcrm-postgres -e POSTGRES_PASSWORD=mysecretpassword  -e POSTGRES_USER=djcrm -e POSTGRES_DB=djcrm -p 5432:5432 -d postgres

$ export READ_DOT_ENV_FILE=True

$ python3 -m virtualenv env -p python3 --always-copy

$ source env/bin/activate

(env) $ pip install -r requirements.txt

(env) $ python manage.py migrate

(env) $ python manage.py createsuperuser

(env) $ python manage.py runserver
```

## Production

Important: review and change credential values accordingly.

Build the image and create a network:
```shell
$ docker build -t crm-django:latest .

$ docker network create djcrm
```
Create the database:
```shell
$ docker run --name djcrm-postgres --network djcrm -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_USER=djcrm -e POSTGRES_DB=djcrm -d postgres
```

Start the container:
```shell
$ docker run --name djcrm -d -e ALLOWED_HOST=* \
    -e DEBUG=False \
    -e SECRET_KEY='enter-value-here' \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -e POSTGRES_USER=djcrm \
    -e POSTGRES_DB=djcrm \
    -e POSTGRES_HOST=djcrm-postgres \
    -e POSTGRES_PORT=5432  \
    -p 80:8000 \
    --network djcrm \
    crm-django:latest
```

To create the super user:
```shell
$ docker exec -it djcrm python manage.py createsuperuser
```

### Add SSL

Create certificates:

```shell
$ sudo openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:2048 -out /etc/ssl/certs/crm.key
$ sudo openssl req -x509 -key /etc/ssl/certs/crm.key -out /etc/ssl/certs/crm.crt -days 360 -addext "subjectAltName = DNS:*"
```
Note: use certbot to generate valid certificates.

Start the container (change certificates path if needed):

```shell
$ docker run --name djcrm -d -e ALLOWED_HOST=* \
    -e DEBUG=False \
    -e SECRET_KEY='enter-value-here' \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -e POSTGRES_USER=djcrm \
    -e POSTGRES_DB=djcrm \
    -e POSTGRES_HOST=djcrm-postgres \
    -e POSTGRES_PORT=5432  \
    -e SSL_FLAG=True \
    -v /etc/ssl/certs/crm.key:/etc/ssl/certs/crm.key \
    -v /etc/ssl/certs/crm.crt:/etc/ssl/certs/crm.crt \
    -p 443:8000 \
    --network djcrm \
    crm-django:latest
```

### Add SMTP

Add SMTP credentials:

```shell
$ docker run --name djcrm -d -e ALLOWED_HOST=* \
    -e DEBUG=False \
    -e SECRET_KEY='enter-value-here' \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -e POSTGRES_USER=djcrm \
    -e POSTGRES_DB=djcrm \
    -e POSTGRES_HOST=djcrm-postgres \
    -e POSTGRES_PORT=5432  \
    -e SMTP_FLAG=True \
    -e EMAIL_HOST= \
    -e EMAIL_HOST_USER= \
    -e EMAIL_HOST_PASSWORD= \
    -e EMAIL_PORT= \
    -e DEFAULT_FROM_EMAIL= \
    -e SSL_FLAG=True \
    -v /etc/ssl/certs/crm.key:/etc/ssl/certs/crm.key \
    -v /etc/ssl/certs/crm.crt:/etc/ssl/certs/crm.crt \
    -p 443:8000 \
    --network djcrm \
    crm-django:latest
```