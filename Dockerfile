FROM python:3.7-slim

RUN apt-get update; apt-get upgrade -y; apt-get install build-essential git -y

RUN pip3 install --upgrade malwareconfig starlette uvicorn

COPY ./app /app

RUN git clone --recursive https://github.com/VirusTotal/yara-python ;\
    cd yara-python ;\
    python3 setup.py build --enable-magic --enable-dotnet ;\
    python3 setup.py install

ENTRYPOINT ["/app/start.sh"]