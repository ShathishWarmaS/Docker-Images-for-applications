FROM ubuntu:20.04

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y python3

CMD ["python3", "app.py"]
