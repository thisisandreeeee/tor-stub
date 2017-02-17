from __future__ import print_function
from stem import Signal, SocketError
from stem.control import Controller
import requesocks
import requests
import json
import time

def regular_request(url):
    r = requests.get(url)
    if r.status_code == 200:
        _parse_and_print_response(r)

def tor_request(url, num_iter=3):
    sessions = requesocks.session()
    sessions.proxies = {
        'http': 'socks5://localhost:9050',
        'https': 'socks5://localhost:9050'
    }
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            for i in range(num_iter):
                s = sessions.get(BASE_URL)
                if s.status_code == 200:
                    _parse_and_print_response(s)
                controller.signal(Signal.NEWNYM)
                time.sleep(2)
                print("- refresh -")
    except SocketError, e:
        print(e, '\nPlease start Tor first.')

def _parse_and_print_response(r):
    try:
        data = r.json()
    except:
        data = json.loads(r.text)
    ip, city = data['ip'], data['city']
    if not city:
        city = data['country_name']
    else:
        city += ', {}'.format(data['country_name'])
    print("{} in {}".format(ip, city))

if __name__=="__main__":
    BASE_URL = 'http://freegeoip.net/json/'
    print("Making regular request")
    regular_request(BASE_URL)
    print("Now making tor requests")
    tor_request(BASE_URL)
