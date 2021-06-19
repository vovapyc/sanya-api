FROM python:3.8-slim

WORKDIR ./app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./api ./api
COPY ./db ./db
COPY ./helpers ./helpers
COPY ./main.py ./
COPY ./config.py ./

CMD ["python", "main.py"]
