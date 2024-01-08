FROM python:3.8.5

WORKDIR /src

COPY requirements.txt .

RUN pip install -- upgrade pip

RUN pip install -r requirements.txt

COPY src/ .

ENV PYTHONPATH=./:./APP

EXPOSE 8000

CMD [ "bash", "run.sh" ]