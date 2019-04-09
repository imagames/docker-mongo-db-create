FROM python:3-alpine
LABEL maintainer="alvaro.brey@imagames.com"

COPY requirements.txt /requirements.txt
COPY run.py /run.py

RUN python3 -m pip install -r /requirements.txt --no-cache-dir

CMD ["/run.py"]
