FROM python:3.9.18-slim-bookworm

WORKDIR /python-docker

# COPY server/djangoapp/microservices/requirements.txt requirements.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# COPY server/djangoapp/microservices/. .
COPY . .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0           

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
