FROM python:3.11
WORKDIR /app
COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -U pipenv==2023.8.20
RUN pipenv install
RUN apt-get update
RUN pip install pypdf

ENV PYTHONPATH=$PATHONPATH:`pwd`
CMD pipenv run bash