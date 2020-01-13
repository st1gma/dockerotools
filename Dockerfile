FROM python:3.7
MAINTAINER Juan <juan@jmp-esp.net>

RUN apt update ;\
    apt upgrade -y ;\
    apt install apt-transport-https ca-certificates wget dirmngr gnupg software-properties-common wget -y;\
    wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | apt-key add - ;\
    add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/ ;\
    add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/ ;\
    apt update ;\
    apt install adoptopenjdk-8-hotspot build-essential git -y

RUN pip3 install --upgrade malwareconfig starlette uvicorn pycrypto pefile

COPY ./app /opt/app
COPY ./decoders /opt/decoders

RUN git clone --recursive https://github.com/VirusTotal/yara-python ;\
    cd yara-python ;\
    python3 setup.py build --enable-magic --enable-dotnet ;\
    python3 setup.py install

ENTRYPOINT ["/opt/app/start.sh"]