FROM python:3.8.7-alpine

WORKDIR /app

COPY . .

RUN pip install asciimatics

CMD [ "python", "./game.py" ]