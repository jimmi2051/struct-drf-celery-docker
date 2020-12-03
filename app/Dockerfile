# pull official base image
FROM python:3.8-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . /usr/src/app/

RUN pip install pipenv

RUN pipenv install --ignore-pipfile

# lint
RUN pip install flake8
RUN flake8 --ignore=E501,F401 .

# # run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]