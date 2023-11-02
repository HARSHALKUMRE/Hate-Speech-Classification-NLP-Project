FROM python:3.10-slim-bullseye

RUN apt update -y && apt install ffmpeg -y

RUN pip install --upgrade setuptools

RUN pip --no-cache-dir install --upgrade awscli

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]