import requests

from flask import Flask

app = Flask(__name__)

BUS_TIME_API_KEY = 'f503eed0-8041-4e63-933c-6e622563ce18'
URL = 'http://bustime.mta.info/api/siri/stop-monitoring.json'
PAYLOAD = {'key':BUS_TIME_API_KEY, 'OperatorRef':'MTA', 'MonitoringRef':'403303'} 

@app.route('/v1/bustime/m9')
def m9():
    payload = PAYLOAD.update({'LineRef':'MTA NYCT_M9'})
    r = requests.get(URL, params=PAYLOAD)
    print(r)
    print(r["Siri"])
    return True


def m21():
    return True


if __name__ == "__main__":
    m9()
