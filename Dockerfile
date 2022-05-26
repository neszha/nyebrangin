FROM python:3.10

COPY . game

RUN apt-get update
RUN apt-get install python3-pygame -y
RUN pip install pygame

WORKDIR "/game"

ENV DISPLAY=host.docker.internal:0.0

CMD ["python3", "./nyebrangin.py"]