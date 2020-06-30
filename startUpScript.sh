#!/bin/bash

# start MongoDB
mongodb-linux-x86_64-3.2.22/bin/mongod &
sleep 10s
echo "MongoDB started"

python3 /assignment.py
