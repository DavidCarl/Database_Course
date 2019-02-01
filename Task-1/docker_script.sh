#!/bin/bash
touch docker.db
docker run -v $PWD/docker.db/:/home/simple.db davidcarl/database_course:Task-1 python ./main.py "$@"
