# Docker-o-tools

It's simply a docker container to run several decoders. 

All the credit goes to the following awesome dudes:

KevinTheHermit -> https://github.com/kevthehermit
jurg -> https://github.com/jurg
sysopfb -> https://github.com/sysopfb

## How to run

```
$ git clone https://github.com/st1gma/dockerotools.git
$ cd dockerotools
$ sudo docker-compose build
$ sudo docker-compose up
```
## Hot to use

It is a simple REST (unfinished) interface so any HTTP request to the correct endpoint will receive the answer required.
```
$ curl -s http://dockerotools:8000/malwareconfig/8a497a3f376e4a59a2d4243ee1ccf3a33fab9c3c39280faa5e943aeb2cbe9c74 | jq -r
{
  "config": {
    "MUTEX": "DC_MUTEX-ECE4D3X",
    "SID": "stub_2",
    "FWB": "0",
    "NETDATA": "127.0.0.1:200|sbyclaudl.ddns.net:1235|pluewredw.chickenkiller.com:1235|groaqohtw.duckdns.org:1212",
    "GENCODE": "mGkzKdEvv1NN",
    "INSTALL": "1",
    "COMBOPATH": "10",
    "EDTPATH": "temp_4808591720191748\\svchost.exe",
    "KEYNAME": "Mupdate_4808591720191748",
    "EDTDATE": "16/04/2007",
    "PERSINST": "1",
    "MELT": "0",
    "CHANGEDATE": "0",
    "DIRATTRIB": "6",
    "FILEATTRIB": "6",
    "SH1": "1",
    "SH5": "1",
    "SH6": "1",
    "PERS": "1",
    "OFFLINEK": "1",
    "Version": "#KCMDDC51#-890",
    "mal_family": "DarkComet"
  }
}

```