![example workflow](https://github.com/pkrfc/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Описание проекта:

```
Yamdb — сервис-отзовик. Проект собирает отзывы пользователей на произведения. 
Произведения делятся на категории: «Книги», «Фильмы», «Музыка».Список категорий может быть расширен администратором.
В каждой категории есть произведения: книги, фильмы или музыка. 
Произведению может быть присвоен жанр. Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы.
Стек технологий: python, django, DRF, git, sqlite
```

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:pkrfc/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```


Запустите docker-compose
```
cd infra/
docker-compose up -d
```

Выполните миграции, создайте суперпользователя, перенесите статику:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

Ссылка на проект:

http://84.252.141.245:5000/