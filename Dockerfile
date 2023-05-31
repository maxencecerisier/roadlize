FROM python:3.8
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .