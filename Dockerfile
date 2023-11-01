FROM google/cloud-sdk:410.0.0

WORKDIR /src/hatespeechClassifier   
COPY . /src/hatespeechClassifier

RUN apt update -y && \
    apt-get update && \
    pip install --upgrade pip && \
    apt-get install ffmpeg libsm6 libxext6 -y


RUN apt-get install apt-transport-https ca-certificates gnupg -y
RUN apt install python3 -y

RUN pip install -r requirements.txt 

CMD ["python3", "app.py"]