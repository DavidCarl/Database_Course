FROM python:3

COPY /Task-1/main.py /home/main.py
COPY /Task-1/custom_json.py /home/custom_json.py
COPY /Task-1/requirements.txt /home/requirements.txt

RUN chmod 755 /home/main.py
RUN pip install -r /home/requirements.txt
RUN touch simple.db

WORKDIR /home/

# CMD [ "python3", "/home/main.py" ]
