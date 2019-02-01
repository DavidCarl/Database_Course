#!/bin/bash
touch docker.db
docker run -v $PWD/docker.db/:/home/simple.db davidcarl/database_task_1:latest python ./main.py "$@"