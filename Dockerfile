# Use a imagem base desejada
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos necessários para dentro do container
COPY . /app

# Instalação das dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Instalação do cron e ajustes necessários
RUN apt-get update \
    && apt-get -y install cron \
    && rm -rf /var/lib/apt/lists/*

# Adiciona o arquivo crontab com o job
ADD cronjob /etc/cron.d/cronjob

# Permissões no arquivo crontab
RUN chmod 0644 /etc/cron.d/cronjob

# Cria o arquivo de log cron
RUN touch /var/log/cron.log

# CMD para iniciar o cron em segundo plano e a aplicação Python em primeiro plano
CMD service cron start && python /app/app.py
