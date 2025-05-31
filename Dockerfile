# Бесплатный курс по Docker
# https://karpov.courses/docker
# не рекламы ради - сам проходил этот курс :)
#
# используем легковесный образ python 3.11
FROM python:3.11-slim

# устанавливаем системные зависимости для SSH
# и чистим кэш пакетов для оптимизации размера образа
RUN apt-get update && apt-get install -y openssh-client && rm -rf /var/lib/apt/lists/*

RUN mkdir -p ~/.ssh
RUN cat <<EOF > ~/.ssh/config
Host cisco-sw
    HostName cisco-sw
    User cisco
    KexAlgorithms diffie-hellman-group-exchange-sha1
    HostKeyAlgorithms ssh-rsa
EOF

RUN chmod 600 ~/.ssh/config

# устанавливаем рабочую директорию в /app
WORKDIR /app

# копируем все файлы из корневой директории в /app
COPY . .

# устанавливаем зависимости из requirements.txt
RUN pip install -r requirements.txt

# пробрасываем порт 5000 из контейнера наружу
EXPOSE 5000

# запускаем приложение при старте контейнера
CMD ["gunicorn", "--log-level", "debug", "app:app", "--bind", "0.0.0.0:5000"]
