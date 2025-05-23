# Бесплатный курс по Docker
# https://karpov.courses/docker
# не реклама, сам проходил этот курс :)
#
# используем легковесный образ python 3.11
FROM python:3.11-slim

# устанавливаем рабочую директорию в /app
WORKDIR /app

# копируем все файлы из корневой директории в /app
COPY . .

# устанавливаем зависимости из requirements.txt
RUN pip install -r requirements.txt

# пробрасываем порт 5000 из контейнера наружу
EXPOSE 5000

# запускаем приложение при старте контейнера
CMD ["python", "app.py"]