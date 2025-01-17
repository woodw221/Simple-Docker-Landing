FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
COPY ./app /app
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH ~/Desktop/Project/Flask/app/static
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
