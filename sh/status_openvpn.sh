#!/bin/bash
export PYTHONIOENCODING=UTF-8
/var/vpn_stat/sh/my_sudo /var/vpn_stat/sh/openvpn_status.py > /dev/shm/vpn.status
chmod 666 /dev/shm/vpn.status