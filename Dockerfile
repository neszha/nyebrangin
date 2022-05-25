FROM python:3.10

COPY . game

RUN apt update
RUN pip install pygame

WORKDIR "/game"

CMD ["python", "./nyebrangin.py"]