# justip.info

Justip.info is simple web-application for determining information about your public IP and location.

All data returned as plain text, so can be accessed enywhere even from the command line.

There are few choices available:

- [justip.info] (http://justip.info) - returns your public IP address:
```
[ec2-user@justip ~]$ curl justip.info
54.93.225.2
```
- [justip.info/full] (http://justip.info/full) - returns your public IP address and location information:
```
[ec2-user@justip ~]$ curl justip.info/full
continent_code: EU
country_code: DE
country_code3: DEU
country_name: Germany
region: 05
city: Frankfurt
postal_code: 65931
latitude: 50.11669921875
longitude: 8.6833000183105
dma_code: 0
area_code: 0
asnum: AS16509 Amazon.com, Inc.
```
- [justip.info/lookup/X.X.X.X] (http://justip.info/lookup/8.8.8.8) - returns information about specific IP address:
```
[ec2-user@justip ~]$ curl justip.info/lookup/8.8.8.8
continent_code: NA
country_code: US
country_code3: USA
country_name: United States
region: CA
city: Mountain View
postal_code: 94040
latitude: 37.384498596191
longitude: -122.08809661865
dma_code: 807
area_code: 650
```
- [justip.info/about] (http://justip.info/about) - basic info

This product includes GeoLite data created by MaxMind, available from http://www.maxmind.com.
