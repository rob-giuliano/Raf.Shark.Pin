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

import re
import urllib.parse
import urllib.error
import urllib.request
import argparse
from libs.rShark import *


class sharkCheck:
    def __init__(self, loanshark, sharkloader,  sharkcheck, cls, vuln, *args, **kwargs):
        self.loanshark = loanshark
        self.sharkloader = sharkloader
        self.sharkcheck = sharkcheck
        self.cls = cls
        self.vuln = vuln

varShark_C = sharkCheck('loanRsk', 'loadeRsk', 'checkRsk', 'clsRsk', 'vulnRsk')
raf_shark_load = varShark_C
raf_shark_check = varShark_C


def rFodera(target, raf_shark_load, raf_shark_check):
    check_target = urllib.request.urlopen(target)
    rshark_stat = 0
    if check_target.code == 999:
        print("[RSP -Info]", "Detect Waf!")
        time.sleep(3)
    for params in target.split("?")[1].split("&"):
        for varShark_C.loanshark in  varShark_C.sharkloader:
            varShark_C.vuln = target.replace(params, params + str(varShark_C.loanshark).strip())
            request = user_agent.open(varShark_C.vuln)
            html = request.readlines()
            for line in html:
                varShark_C.cls = re.findall(varShark_C.sharkcheck, line.decode('cp1252'))
                if len(varShark_C.cls) != 0:
                    print(" ")
                    print(srkColor.bold(1), "[RSP - Scan]: >>> Audit Snippet >>> " + varShark_C.vuln)
                    print(srkColor.bold(1) + "\t", "=================================================" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|                                               |" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|", '[RSP - Info]: >>> Target is  vulnerable!', '\t', "|" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|                                               | " + srkColor.end())
                    print(srkColor.bold(1) + "\t", "=================================================" + srkColor.end())
                    print(" ")


                    rshark_stat += 1
    if rshark_stat == 0:
        print("\t", srkColor.bold(1), "%s %s" % (" [RSP - Info]: >>>  Web target is not vulnerable!"))
    else:
        print("")
        print(srkColor.blue(1))
        print(banner, srkColor.end())
        print("\t", srkColor.cyan(1), "[RSP - Info]: >>>  Scan completed", srkColor.end())
        print("\t", srkColor.cyan(1), "[RSP - Info]: >>>  Target: ", srkColor.end(), srkColor.bold(1), target, srkColor.end())
        print(" ")
        print("\t")
        print(srkColor.bold(1) + "\t", "=================================================" + srkColor.end())
        print(srkColor.bold(1) + "\t", "|", '\t', '\t', ('Raport Scan'), "\t", "\t", "\t", "|", "\t" + srkColor.end())
        print(srkColor.bold(1) + "\t", "|                                               |" + srkColor.end())
        print(srkColor.bold(1) + "\t", "|                                               |" + srkColor.end())
        print(srkColor.bold(1), "\t",  "|", '\t', "Full Found: %i bugs."  %(rshark_stat),"\t", "\t", "\t", "|", "\t" + srkColor.end())
        print(srkColor.bold(1) + "\t", "|                                               | " + srkColor.end())
        print(srkColor.bold(1) + "\t", "|                                               | " + srkColor.end())
        print(srkColor.bold(1) + "\t", "=================================================" + srkColor.end())
        print(srkColor.bold(1))
        print(srkColor.end())



class sharkSec:
    def __init__(self, rcce, waf, xxs, sqli, ckdir):
        self.rcce = rcce
        self.waf = waf
        self.xxs = xxs
        self.sqli = sqli
        self.ckdir = ckdir

varSec = sharkSec('raf_sec_rcce', 'raf_sec_waf', 'rafy_sec_xxs', 'raf_sec_sqli', 'raf_sec_ckdir')
varChecker = sharkSec('raf_check_rcce', 'raf_check_waf', 'rafy_check_xxs', 'raf_check_sqli', 'raf_check_ckdir')

def sharky_rce_test_full(target):
    headers_reader(target)
    print(" ")
    print("\t", srkColor.bold(1), ("[RSP - Info:] Target: " + target), srkColor.end())
    print(" ")
    print(" ")
    print(srkColor.bold(1), "[RSP - Info]: >>> [Modx PenTester] >>> Remote Code Execution")
    time.sleep(3)
    varSec.rcce = open("libs/rSec/rcce.txt", "r").readlines()
    varShark_C.sharkloader = varSec.rcce
    varChecker.rcce = open("libs/rChecker/_checker_rcce.txt", "r").readline()
    varShark_C.sharkcheck = re.compile(varChecker.rcce, re.I)
    rFodera(target, raf_shark_load, raf_shark_check)


def sharky_waf_test_full(target):
    headers_reader(target)
    print(" ")
    print("\t", srkColor.bold(1), ("[RSP - Info:] Target: " + target), srkColor.end())
    print(" ")
    print(" ")
    print(srkColor.bold(1), "[RSP - Info]: >>> [Modx PenTester] >>> DIOS WAF Bypassed")
    time.sleep(3)
    varSec.waf = open("libs/rSec/waf.txt","r").readlines()
    varShark_C.sharkloader = varSec.waf
    varChecker.waf = open("libs/rChecker/_checker_waf.txt", "r").readline()
    varShark_C.sharkcheck = re.compile(varChecker.waf, re.I)
    rFodera(target, raf_shark_load, raf_shark_check)


def sharky_xxs_test_full(target):
    headers_reader(target)
    print(" ")
    print("\t", srkColor.bold(1), ("[RSP - Info:] Target: " + target), srkColor.end())
    print(" ")
    print(" ")
    print(srkColor.bold(1), "[RSP - Info]: >>> [Modx PenTester] >>> Xss Vulnerability")
    time.sleep(3)
    varSec.xxs = open("libs/rSec/xxs.txt", "r").readlines()
    varShark_C.sharkloader = varSec.xxs
    varChecker.xxs = open("libs/rChecker/_checker_xxs.txt", "r").readline()
    varShark_C.sharkcheck = re.compile(varChecker.xxs, re.I)
    rFodera(target, raf_shark_load, raf_shark_check)


def sharky_sqli_test_full(target):
    headers_reader(target)
    print(" ")
    print("\t", srkColor.bold(1), ("[RSP - Info:] Target: " + target), srkColor.end())
    print(" ")
    print(" ")
    print(srkColor.bold(1), "[RSP - Info]: >>> [Modx PenTester] >>> SQL Injection")
    time.sleep(3)
    varSec.sqli = open("libs/rSec/sqli.txt","r").readlines()
    varShark_C.sharkloader = varSec.sqli
    varChecker.sqli = open("libs/rChecker/_checker_sqli.txt", "r").readline()
    varShark_C.sharkcheck = re.compile(varChecker.sqli, re.I)
    rFodera(target, raf_shark_load, raf_shark_check)
