FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y cron

COPY crontab /etc/cron.d/my-cron-job

RUN chmod 0644 /etc/cron.d/my-cron-job
RUN crontab /etc/cron.d/my-cron-job

CMD ["cron", "-f"]
