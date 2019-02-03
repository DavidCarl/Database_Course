#!/bin/bash
touch docker.db
docker run -v $PWD/simple.db:/home/simple.db davidcarl/database_course:Task-1 python /home/main.py "$@"
