# justip.info

Justip.info is simple web-application for determining information about your public IP and location.

All data returned as plain text, so can be accessed enywhere even from the command line.

There are few choices available:

- [justip.info] (http://justip.info) - returns your public IP address:
```
[ec2-user@justip ~]$ curl justip.info
54.93.215.130
```
- [justip.info/full] (http://justip.info/full) - returns your public IP address and location information:
```
[ec2-user@justip ~]$ curl justip.info/full
city: Frankfurt
region_name: Hessen
region: 05
area_code: 0
time_zone: Europe/Berlin
longitude: 8.68330001831
metro_code: 0
country_code3: DEU
latitude: 50.1166992188
postal_code: 60438
dma_code: 0
country_code: DE
country_name: Germany
asnum: AS16509 Amazon.com, Inc.
```
- [justip.info/lookup/X.X.X.X] (http://justip.info/lookup/8.8.8.8) - returns information about specific IP address:
```
[ec2-user@justip ~]$ curl justip.info/lookup/8.8.8.8
city: Mountain View
region_name: California
region: CA
area_code: 650
time_zone: America/Los_Angeles
longitude: -122.08380127
metro_code: 807
country_code3: USA
latitude: 37.3860015869
postal_code: 94035
dma_code: 807
country_code: US
country_name: United States
asnum: AS15169 Google Inc.
```
- [justip.info/about] (http://justip.info/about) - basic info

This product includes GeoLite data created by MaxMind, available from http://www.maxmind.com.
