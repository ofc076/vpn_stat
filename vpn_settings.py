# -*- coding: utf-8 -*-
OS = 'linux'
#OS = 'windows'
DEV = False
if OS.lower() == 'linux':
    STATUS_FILE_PATH = '/dev/shm/vpn.status' #

else:
    STATUS_FILE_PATH = 'D:\\TEST-2\\vpn.status'
STATUS_CMD = '/var/vpn_stat/sh/status_openvpn.sh'
REFRESH_TIME = '30'    # in second
