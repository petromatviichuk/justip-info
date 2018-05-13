from flask import Flask, request, url_for
import GeoIP
import socket

app = Flask(__name__, static_url_path='/static')

geoipcity="GeoLiteCity.dat"
geoipasnum="GeoIPASNum.dat"

#Get information about IP address from GeoIP database
def ipdata(ipaddr):
    ipfull = GeoIP.open(geoipcity, GeoIP.GEOIP_STANDARD)
    ipasn = GeoIP.open(geoipasnum, GeoIP.GEOIP_STANDARD)
    ip = ipfull.record_by_name(ipaddr)
    asn = ipasn.name_by_addr(ipaddr)
    ip['asnum'] = asn

    data=""
    for key, value in ip.items():
        data = data + str(key) + ": " + str(value) + "\n"
    return data,{'Content-Type': 'text/plain; charset=utf-8'}

@app.route('/')
def iponly():
 if request.headers.getlist("X-Forwarded-For"):
   ip = request.headers.getlist("X-Forwarded-For")[0]
 else:
   ip = request.remote_addr
 return ip + '\n', {'Content-Type': 'text/plain; charset=utf-8'}

@app.route('/full')
def ipfull():
 if request.headers.getlist("X-Forwarded-For"):
   ip = request.headers.getlist("X-Forwarded-For")[0]
 else:
   ip = request.remote_addr
 return ipdata(ip) 

#Validate IP address and return information
@app.route('/lookup/<ipaddr>')
def iplookup(ipaddr):
    try:
        socket.inet_pton(socket.AF_INET, ipaddr)
    except socket.error:
        return 'Wrong IP address!' + '\n'
        exit(1)
    return ipdata(ipaddr)

@app.route('/about')
def about():
 return 'Check your IP easily \nMore information here: https://github.com/pmatv/justip-info \n\
Made by Petro Matviichuk (petro@matviichuk.com)\n',{'Content-Type': 'text/plain; charset=utf-8'}

@app.route('/robots.txt')
def robots():
 return app.send_static_file('robots.txt')

@app.route('/favicon.ico')
def icon():
 return app.send_static_file('favicon.ico')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
