# Base Imaghe
FROM python:3.9

ENV PYTHONBUFFERED 1

RUN mkdir /code

WORKDIR /code

# copy pipfile and pipfile.lock
COPY Pipfile Pipfile.lock ./

# install pipenv on the container
RUN pip install -U pipenv

# install project dependencies
RUN pipenv install --system

# copy all files and directories from <src> to <dest>
COPY . .

# expose the port
EXPOSE 8000

# Command to run
CMD ["python", "devsearch/manage.py", "runserver", "0.0.0.0:8000"]
