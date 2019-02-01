FROM python:3

COPY main.py /home/main.py
COPY custom_json.py /home/custom_json.py
COPY requirements.txt /home/requirements.txt

RUN chmod 755 /home/main.py
RUN pip install -r /home/requirements.txt
RUN touch simple.db

WORKDIR /home/

# CMD [ "python3", "/home/main.py" ]