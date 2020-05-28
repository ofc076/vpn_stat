#!/usr/bin/python3
# -*- coding: utf-8 -*-
# open_vpn status parsing
CLIENTDICT = {'650000':'myRPi', 
            '710100':'Черкасы-1', 
            '260100':'Ів.-Франк.-1',
            '264200':'Ів.-Франк.-2',
            '710700':'Сміла (крон)',
            '711800':'Корс.-Шевч. (крон)',
            '710200':'Умань',
            '712000':'Черкасы-2',
            '488100':'"Орион"-S.O.E.',
            '460280':'Львов-2 (kiosk)',
            '460281':'Львов-2 (kiosk-2)',
            '770400':'Черновцы-4',
            '261100':'Коломия',
            '511600':'Bolgrad',
            '560100':'Rovno',
            '710800':'Жашков',
            '488101':'"Орион"-Tablo'}
PATH = '/var/run/openvpn.server.status'
#import os
#os.environ['LANG'] = 'ru_UA.UTF-8'
#os.environ['PYTHONIOENCODING'] = 'UTF-8'
#print(os.environ)
try:
    with open(PATH, 'r') as f:
        arr = f.readlines()
except:
    print('OpenVPN NOT ACTIVE !!!')
    exit()
# print(txt)
txt = []
for line in arr:
    txt.append(line.replace('\n',''))
count = 0
numClientListStr = 0
numRouteTableStr = 0
numGlobalStatStr = 0
for line in txt:
    if not line.find("OpenVPN CLIENT LIST") == -1:
        numClientListStr = count
    if "ROUTING TABLE" in line:
        numRouteTableStr = count
    if "GLOBAL STATS" in line:
         numGlobalStatStr = count
    count += 1

clientList = txt[numClientListStr + 3: numRouteTableStr]
clientArr = []
for line in clientList:
    clientArr.append(line.split(','))
routeTable = txt[numRouteTableStr + 2: numGlobalStatStr]
routeArr = []
for line in routeTable:
    routeArr.append(line.split(','))
if not len(clientArr) == len(routeArr):
    print('=== ERROR !!! ===')
    exit()
clientSorted = sorted(clientArr, key=lambda client: client[0])
routeSorted = sorted(routeArr, key=lambda route: route[1])
zipped = zip(clientSorted, routeSorted)
total = []
for line in zipped:
    for route in line[1]:
        line[0].append(route)
    clientName = CLIENTDICT.get(line[0][0], '******')
    line[0].append(clientName)
    total.append(line[0])
print(txt[1])
print('----------------------------------------------------------')
for line in total:
#    print(line)
    print('{:14}  |  {}  |  {:14}   |  {}'.format(line[-1], line[0], line[5], line[8]))
print('----------------------------------------------------------')


exit()
