FROM python:3.9

ENV PYTHONBUFFERED 1

RUN pip install pipenv

COPY Pipfile Pipfile.lock

RUN pipenv install

COPY . ./code

WORKDIR /code/devsearch

CMD ["python", "manage.py", "runserver"]
