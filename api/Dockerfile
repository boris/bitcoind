FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y python3-dev build-essential

RUN mkdir /code
WORKDIR /code
EXPOSE 5001

ADD . /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
