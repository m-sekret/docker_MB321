#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static
cp sample_app.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

#Dockerfile
echo "FROM python" >> tempdir/Dockerfile

echo "RUN pip install flask" >> tempdir/Dockerfile

echo "WORKDIR /home/myapp" >> tempdir/Dockerfile

echo "COPY ./static ./static/" >> tempdir/Dockerfile
echo "COPY ./templates ./templates/" >> tempdir/Dockerfile
echo "COPY sample_app.py ./" >> tempdir/Dockerfile

echo "EXPOSE 8080" >> tempdir/Dockerfile

echo "CMD python3 ./sample_app.py" >> tempdir/Dockerfile

cd tempdir
docker build -t sampleapp .
docker run -t -d -p 8080:8080 --name samplerunning sampleapp

docker ps -a
