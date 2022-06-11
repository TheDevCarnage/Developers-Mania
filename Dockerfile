# Base Image
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

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

# copy all files and directories from <src> to <dest>
COPY . .

ENTRYPOINT ["/devsearch/entrypoint.sh"]
