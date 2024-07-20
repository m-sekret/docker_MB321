#!/bin/bash

echo "Enter port: "
read port

docker run -t -d -p $port:8080 --name samplerunning sampleapp
docker ps -a
