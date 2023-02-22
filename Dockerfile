FROM ubuntu:latest

RUN apt-get update && apt-get install python3 -y && apt-get install python3-pip -y


WORKDIR /app
COPY . .

RUN pip install setup.py

RUN flask --app lineage_classes init-db


EXPOSE 8000


CMD ["gunicorn", "-w 4","-b 0.0.0.0", "lineage_classes:create_app()"]
