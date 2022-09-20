FROM python:3.9-slim-buster
WORKDIR /service
RUN python3 -m pip install --upgrade pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
#RUN apt-get update
#RUN apt-get install nano
COPY server.py /service
ENTRYPOINT ["python3"]
CMD ["server.py"]