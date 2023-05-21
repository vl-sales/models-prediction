FROM python:3.10.6-slim-buster
# evitar compilação travada devido ao prompt do usuário
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /models-api

COPY . .

RUN apt-get update
RUN pip install --upgrade pip
RUN apt-get install -y libgl1-mesa-glx
RUN apt-get update && apt-get install -y libglib2.0-0
RUN apt-get -y install poppler-utils
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python"]
CMD ["main.py"]