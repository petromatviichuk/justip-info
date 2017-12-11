FROM python:alpine

RUN apk --update add geoip-dev gcc musl-dev
RUN pip install flask geoip

RUN wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
RUN wget http://download.maxmind.com/download/geoip/database/asnum/GeoIPASNum.dat.gz
RUN gunzip GeoLiteCity.dat.gz
RUN gunzip GeoIPASNum.dat.gz

COPY static /opt/static
COPY justipinfo.py /opt

EXPOSE 5000

ENTRYPOINT ["python", "/opt/justipinfo.py"]
