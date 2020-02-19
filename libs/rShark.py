####################################################################
# Python 3.6.8
# Project Name: RAF SHARK PIN
# ver  1.0
# Developer: ROB GIULIANO  -a.k.a- PG
# Etherium:       0x14996EE0113C46A34b14e4F30197768b174c9486
# Bitcoin:        1HN7eNRiJFWR1JXQdMx2hwVCaANmbhnUrb
# Bitcoin Cash:   qz7h44sqpn8ud2hv04tw2kgr9ayqu94gngm2tedvrt
# Tipeeestream:   https://www.tipeeestream.com/rob-giuliano/donation
#####################################################################


import time
from libs.rColor import *
import urllib.request
from urllib.request import FancyURLopener


banner = r"""
               ____        __               __            _
   _________ _/ __/  _____/ /_  ____ ______/ /__   ____  (_)___
  / ___/ __ `/ /_   / ___/ __ \/ __ `/ ___/ //_/  / __ \/ / __ \
 / /  / /_/ / __/  (__  ) / / / /_/ / /  / ,<    / /_/ / / / / /
/_/   \__,_/_/    /____/_/ /_/\__,_/_/  /_/|_|  / .___/_/_/ /_/
                                               /_/
"""


class rand_user_agent(FancyURLopener):
    version = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) ' \
	'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"

user_agent = rand_user_agent()

class varBase:
    def __init__(self, domain, slave):
        self.domain = domain
        self.slave = slave

varWhs = varBase('Dns', 'Cloud')
rSharky_H = varWhs.domain


def headers_reader(target):
    print(srkColor.blue(1))
    print(banner, srkColor.end())
    print("\t", srkColor.bold(1), ("{-fingerprinting-}"))
    print("\t")
    print(" ")

    check_target = urllib.request.urlopen(target)
    if check_target.code == 200:
        print("\t",  "Status code: 200 OK")

    if check_target.code == 404:
        print("\t", "[Info:] Page was not found! Check your target.")
        exit()
    varWhs.slave = check_target.headers.get(rSharky_H)
    varWhs.domain = target.split("/")[2]
    print("\t", "Host: " + str(varWhs.domain) )
    print("\t", "WebServer: " + check_target.headers['Server'])
    print(" ")
    print(" ")
