<h2>Django REST Framework backend for onboarding of new employees<h3/>
 
<h3>Setting up for development:<h4/>
<p><b>Install require packages</b></p>

```shell
pip install -r requirements_dev.txt
```

<p><b>Create folders for env files</b></p>

```shell
mkdir env;
mkdir env/django;
mkdir env/docker;
```

<p><b>Create env files</b></p>
<p>env/docker/.env.db</p>

```dotenv
MYSQL_DATABASE=
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_ROOT_PASSWORD=
```

<p>env/docker/.env.web</p>

```dotenv
ENV_FILE='.env.prod'
DB_PORT=3306 #port exposed in docker-compose file
```

<p>env/django/.env.dev</p>

```dotenv
SECRET_KEY= #can be generated(see below)
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOW_ALL_ORIGINS=True
CORS_ALLOW_CREDENTIALS=True
ROOT_URLCONF=Onboarding.urls
WSGI_APPLICATION=Onboarding.wsgi.application
MYSQL_URL=mysql-connector://(YOUR_USER_NAME):(YOUR_PASSWORD)@localhost:(DB_PORT)/(YOUR_DB_NAME)
DEFAULT_AUTHENTICATION_CLASSES=rest_framework_simplejwt.authentication.JWTAuthentication
LANGUAGE_CODE= # en-us, ru-ru, etc.
TIME_ZONE=UTC
USE_I18N=True
USE_TZ=True
STATIC_URL=static/
STATIC_ROOT=staticfiles
MEDIA_URL=media/
MEDIA_ROOT=media/
DEFAULT_AUTO_FIELD=django.db.models.BigAutoField
AUTH_USER_MODEL=users.CustomUser
ACCESS_TOKEN_LIFETIME=1
REFRESH_TOKEN_LIFETIME=1
ROTATE_REFRESH_TOKENS=False
BLACKLIST_AFTER_ROTATION=False
UPDATE_LAST_LOGIN=False
ALGORITHM=HS256
AUTH_HEADER_TYPES=Bearer,
AUTH_HEADER_NAME=HTTP_AUTHORIZATION
USER_ID_FIELD=id
USER_ID_CLAIM=user_id
USER_AUTHENTICATION_RULE=rest_framework_simplejwt.authentication.default_user_authentication_rule
AUTH_TOKEN_CLASSES=rest_framework_simplejwt.tokens.AccessToken,
TOKEN_TYPE_CLAIM=token_type
TOKEN_USER_CLASS=rest_framework_simplejwt.models.TokenUser
JTI_CLAIM=jti
SLIDING_TOKEN_REFRESH_EXP_CLAIM=refresh_exp
SLIDING_TOKEN_LIFETIME=5
SLIDING_TOKEN_REFRESH_LIFETIME=1
```

<p><b>secret_key generation</b></p>

<p>run following command and copy result in <font color="red">SECRET_KEY</font></p>

```shell
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

<p><b>Run db container and apply all migrations</b></p>

```shell
docker-compose up db -d;
```
```shell
python manage.py makemigrations notifications users welcomejorney;
python manage.py migrate;
```
```shell
docker-compose down;
```

<p><b>Now you are ready to development</b></p>

<p><b>To start db container, run following command</b></p>

```shell
docker-compose up db -d
```

<p><b>To stop</b></p>

```shell
docker-compose down
```

<p><b>Runing development server</b></p>

```shell
python manage.py runserver
```

<p><b>Creating superuser</b></p>

```shell
python manage.py createsuperuser
```

