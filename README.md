# Django REST sample application

TODO sample application made with [Django REST framework](http://www.django-rest-framework.org/).

## Setup

```sh
$ pipenv install
```

## Usage

```sh
$ pipenv shell
$ cd todo
$ ./manage.py migrate
$ ./manage.py createsuperuser
$ ./manage.py runserver
```

Then you can access to the URL: http://localhost:8000/api/v1/tasks/
