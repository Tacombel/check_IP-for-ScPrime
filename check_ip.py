import os
from os.path import exists
import datetime

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

ip = os.popen('curl https://ipinfo.io/ip').read()

if ip == ip_old:
    print(f'La IP sigue siendo {ip_old}')
else:
    print(f'La IP ha cambiado de {ip_old} a {ip}')
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
