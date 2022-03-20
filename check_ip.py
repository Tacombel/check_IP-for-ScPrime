import os
import sys
from os.path import exists
import datetime
from urllib.request import Request, urlopen
from urllib.error import URLError

historico = []
if exists('ip.txt'):
    with open('ip.txt') as f:
        lines = f.readlines()
        for e in lines:
            e = e[:-1]
            e = e.split(',')
            historico.append(e)
        ip_old = historico[-1][1]
else:
    ip_old = 'valor_inicial'

req = Request('https://ipinfo.io/ip')
try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    sys.exit()

ip = response.read()
ip = ip.decode("utf-8")

if ip == ip_old:
    print(f'The IP is still {ip_old}', flush=True)
else:
    print(f'The IP changed from {ip_old} to {ip}', flush=True)
    value = []
    value = [datetime.datetime.now(), ip]
    historico.append(value)
    with open('ip.txt', 'w') as f:
        for h in historico:
            f.write(str(h[0]) + ',' + str(h[1]))
            f.write('\n')
        f.close()
    os.system('docker exec scprime01 spc host announce ' + ip + ':14282' )
    os.system('docker exec scprime02 spc host announce ' + ip + ':24282' )
