FROM python:3.8
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin postgresql-client
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

COPY entrypoint.sh /usr/src/app/
RUN chmod +x /usr/src/app/entrypoint.sh
