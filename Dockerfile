FROM python:3.6
RUN apt-get update
ENV PYTHONUNBUFFERED 1
WORKDIR app
COPY * /app/
RUN pip install -r requirements.txt
CMD gunicorn -b 0.0.0.0:3000 wsgi --reload --log-level DEBUG --workers 5