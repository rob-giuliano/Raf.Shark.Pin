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

from urlvalidator import validate_url
from libs.rFull_Fodera import *
from libs.rFodera import *
from libs.rShark import *
from libs.rColor import *
from libs.ckdir import *
import http.client
import socket


def shark_menu():
    print(srkColor.blue(1))
    print(banner, srkColor.end())
    print(srkColor.bold(1), "\t", " 0. -- Scan -> Full")
    print("\t", " 1. -- Scan -> Remote Code Execution")
    print("\t", " 2. -- Scan -> Xss Vulnerability")
    print("\t", " 3. -- Scan -> SQL Injection")
    print("\t", " 4. -- Scan -> DIOS WAF Bypassed ")
    print("\t", " 5. -- Scan -> Website Directory Scanner")
    print("\t", " +. -- Scan -> Scanning List ", srkColor.end())
    print("")
    print("")
    print("")
    print("")

shark_menu()

class rafStorm:
    def __init__(self, menu, menuChoice1, menuChoice2, stormFunc, *args):
        self.menu = menu
        self.menuChoice1 = menuChoice1
        self.menuChoice2 = menuChoice2
        self.stormFunc = stormFunc

try:
    class StormBase(rafStorm):
        varStorm = rafStorm('choice', 'choice1', 'choice2', 'stormyFunc')



        varStorm.menu = input(" [startx] Make a choice: >>> ")
        if varStorm.menu == "0":
            target = input(" [!] Enter the Target(Ip or Url): ")
            if "?" in target:
                sharky_rce_test_full(target)
                sharky_xxs_test_full(target)
                sharky_sqli_test_full(target)
                sharky_waf_test_full(target)
            else:
                print(srkColor.bold(1))
                print("\t", "[RSP -Info]", "Insert valid URL")
                print("\t", "[RSP - Info]", "You should write target - e.g http://site.com/page.php?id=value")
                print(" ")
                input('         Press Enter to Exit')
                print(srkColor.end())
                exit()

        if varStorm.menu == "1":
            target = input("          Enter the Url: ")
            if "?" in target:
                sharky_rce_test(target)
            else:
                print(srkColor.bold(1))
                print("\t", "[RSP -Info]", "Insert valid URL")
                print("\t", "[RSP -Info]", "You should write target - e.g http://site.com/page.php?id=value")
                print(" ")
                input('         Press Enter to Exit')
                print(srkColor.end())

            exit()

        if varStorm.menu == "2":
            target = input("           Enter the Url: ")
            if "?" in target:
                sharky_xxs_test(target)
            else:
                print(srkColor.bold(1))
                print("\t", "[RSP -Info]", "Insert valid URL")
                print("\t", "[RSP - Info]", "You should write target - e.g http://site.com/page.php?id=value")
                print(" ")
                input('         Press Enter to Exit')
                print(srkColor.end())
            exit()

        if varStorm.menu == "3":
            target = input("          Enter the Url: ")
            if "?" in target:
                sharky_sqli_test(target)
            else:
                print(srkColor.bold(1))
                print("\t", "[RSP -Info]", "Insert valid URL")
                print("\t", "[RSP - Info]", "You should write target - e.g http://site.com/page.php?id=value")
                print(" ")
                input('         Press Enter to Exit')
                print(srkColor.end())
            exit()

        if varStorm.menu == "4":
            target = input("          Enter the Url: ")
            if "?" in target:
                sharky_waf_test(target)
            else:
                print(srkColor.bold(1))
                print("\t", "[RSP -Info]", "Insert valid URL")
                print("\t", "[RSP - Info]", "You should write target - e.g http://site.com/page.php?id=value")
                print(" ")
                input('         Press Enter to Exit')
                print(srkColor.end())
            exit()

        if varStorm.menu == "5":
            try:
                class Ckdir:
                    def __init__(self, raf, shk, pin, opt):
                        self.raf = raf
                        self.shk = shk
                        self.pin = pin
                        self.opt = opt

                varCkdir = Ckdir('rafCheck', 0, 0, 'optMenu')

                try:
                    target = input("       Insert target for scan: ")
                    try:
                        validate_url(target)
                    except ValidationError:
                        raise ValidationError("\t", srkColor.bold(1), "[RSP - Info]", "Insert target  without ('/') - e.g http://site.com")
                    headers_reader(target)
                    if "https" in target:
                        target = target.replace("https://", "")
                    else:
                        target = target.replace("http://", "")
                    print("\t", ("Target: " + target))
                    conn = http.client.HTTPConnection(target)
                    conn.connect()
                    print("\t", "Server status: Acceptable ")

                except socket.error:
                    print(" ")
                    print("\t", srkColor.bold(1), "[RSP - Info]", "Is not - valid Url !!", srkColor.end())
                    print("\t", srkColor.bold(1), "[RSP - Info]", "Insert target  without ('/') - e.g http://site.com")
                    print(" ")
                    input('         Press Enter to Exit')
                    print(" ")
                    exit()
                print(" ")
                print("\t", "=========================")
                print(" ")
                print("\t", "Enter Files 'Hosting' Type:")
                print(" ")
                print("\t", "1 Apache")
                print("\t", "2 Asp.net")
                print("\t", "3 ColdFusion")
                print("\t", "4 Node.js")
                print("\t", "5 CGI Server")
                print("\t", "6 BRF Server")
                print("\t")
                print("\t", " ")
                print("\t")
                varCkdir.opt = eval(input("         >>> :"))

                if varCkdir.opt == 1:
                    print(" ")
                    print("\t", ("[RSP - Info:] Scan: " + target))
                    print(" ")
                    for varCkdir.raf in varOpt_1:
                        varCkdir.raf = varCkdir.raf.replace("\n", "")
                        varCkdir.raf = "/" + varCkdir.raf
                        varWhs.slave = target + varCkdir.raf
                        print(srkColor.bold(1), ("[RSP - Scan]  " + varWhs.slave + "..."))
                        connection = http.client.HTTPConnection(target)
                        connection.request("GET", varCkdir.raf)
                        response = connection.getresponse()
                        varCkdir.pin = varCkdir.pin + 1
                        if response.status == 200:
                            varCkdir.shk = varCkdir.shk + 1
                            print(" ")
                            print("\t", srkColor.cyan(1),
                                  "%s %s" % (" [RSP - Info]: >>>  " + varWhs.slave, " >>> Target found!"),
                                  srkColor.end())
                            print(" ", srkColor.bold(1))
                            print("\t ", srkColor.bold(1), input("           Press 'Enter' to continue scanning."),
                                  srkColor.end())
                            print(" ", srkColor.end())
                        elif response.status == 404:
                            varCkdir.pin = varCkdir.pin
                        elif response.status == 302:
                            print("\t", srkColor.red(1), "%s %s" % (" [RSP - Info]: >>>  " + varWhs.slave,
                                                                    ' >>> Possible {},  in directory (302 - Redirect)'.format(
                                                                        varCkdir.raf.replace("/", ""))), srkColor.end())
                        else:
                            print("\t", srkColor.red(1), "%s %s %s" % (
                            " [RSP - Info]: >>>  " + varWhs.slave, " >>> Server Response:", response.status),
                                  srkColor.end())
                        connection.close()
                    print(" ")
                    print("\t", srkColor.bold(1), " [RSP - Info]: >>>  " + "Scan completed", srkColor.end())
                    print("")
                    print(srkColor.blue(1))
                    print(banner, srkColor.end())
                    print("")
                    print("")
                    print(srkColor.bold(1) + "\t", "=================================================" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|", '\t', '\t', ('Raport Scan'), "\t", "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|                                               |" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|                                               |" + srkColor.end())
                    print(srkColor.bold(1), "\t", "|", "\t", " Target pages found: ", varCkdir.shk, "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1), "\t", "|", "\t", " Raport pages scan:  ", varCkdir.pin, "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1) + "\t",
                          "|                                               | " + srkColor.end())
                    print(srkColor.bold(1) + "\t",
                          "|                                               | " + srkColor.end())
                    print(srkColor.bold(1) + "\t", "=================================================" + srkColor.end())
                    print(srkColor.bold(1))
                    input('         Press Enter to Exit')
                    print(srkColor.end())
                    exit()

                if varCkdir.opt == 2:
                    print(" ")
                    print("\t", ("[RSP - Info:] Scan: " + target))
                    print(" ")
                    for varCkdir.raf in varOpt_2:
                        varCkdir.raf = varCkdir.raf.replace("\n", "")
                        varCkdir.raf = "/" + varCkdir.raf
                        varWhs.slave = target + varCkdir.raf
                        print(srkColor.bold(1), ("[RSP - Scan]  " + varWhs.slave + "..."))
                        connection = http.client.HTTPConnection(target)
                        connection.request("GET", varCkdir.raf)
                        response = connection.getresponse()
                        varCkdir.pin = varCkdir.pin + 1
                        if response.status == 200:
                            varCkdir.shk = varCkdir.shk + 1
                            print(" ")
                            print("\t", srkColor.cyan(1),
                                  "%s %s" % (" [RSP - Info]: >>>  " + varWhs.slave, " >>> Target found!"),
                                  srkColor.end())
                            print(" ", srkColor.bold(1))
                            print("\t ", srkColor.bold(1), input("           Press 'Enter' to continue scanning."),
                                  srkColor.end())
                            print(" ", srkColor.end())
                        elif response.status == 404:
                            varCkdir.pin = varCkdir.pin
                        elif response.status == 302:
                            print("\t", srkColor.red(1), "%s %s" % (" [RSP - Info]: >>>  " + varWhs.slave,
                                                                    ' >>> Possible {},  in directory (302 - Redirect)'.format(
                                                                        varCkdir.raf.replace("/", ""))), srkColor.end())
                        else:
                            print("\t", srkColor.red(1), "%s %s %s" % (
                                " [RSP - Info]: >>>  " + varWhs.slave, " >>> Server Response:", response.status),
                                  srkColor.end())
                        connection.close()
                    print(" ")
                    print("\t", srkColor.bold(1), " [RSP - Info]: >>>  " + "Scan completed", srkColor.end())
                    print("")
                    print(srkColor.blue(1))
                    print(banner, srkColor.end())
                    print("")
                    print("")
                    print(srkColor.bold(1) + "\t", "=================================================" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|", '\t', '\t', ('Raport Scan'), "\t", "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|                                               |" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|                                               |" + srkColor.end())
                    print(srkColor.bold(1), "\t", "|", "\t", " Target pages found: ", varCkdir.shk, "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1), "\t", "|", "\t", " Raport pages scan:  ", varCkdir.pin, "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1) + "\t",
                          "|                                               | " + srkColor.end())
                    print(srkColor.bold(1) + "\t",
                          "|                                               | " + srkColor.end())
                    print(srkColor.bold(1) + "\t", "=================================================" + srkColor.end())
                    print(srkColor.bold(1))
                    input('         Press Enter to Exit')
                    print(srkColor.end())
                    exit()

                if varCkdir.opt == 3:
                    print(" ")
                    print("\t", ("[RSP - Info:] Scan: " + target))
                    print(" ")
                    for varCkdir.raf in varOpt_3:
                        varCkdir.raf = varCkdir.raf.replace("\n", "")
                        varCkdir.raf = "/" + varCkdir.raf
                        varWhs.slave = target + varCkdir.raf
                        print(srkColor.bold(1), ("[RSP - Scan]  " + varWhs.slave + "..."))
                        connection = http.client.HTTPConnection(target)
                        connection.request("GET", varCkdir.raf)
                        response = connection.getresponse()
                        varCkdir.pin = varCkdir.pin + 1
                        if response.status == 200:
                            varCkdir.shk = varCkdir.shk + 1
                            print(" ")
                            print("\t", srkColor.cyan(1),
                                  "%s %s" % (" [RSP - Info]: >>>  " + varWhs.slave, " >>> Target found!"),
                                  srkColor.end())
                            print(" ", srkColor.bold(1))
                            print("\t ", srkColor.bold(1), input("           Press 'Enter' to continue scanning."),
                                  srkColor.end())
                            print(" ", srkColor.end())
                        elif response.status == 404:
                            varCkdir.pin = varCkdir.pin
                        elif response.status == 302:
                            print("\t", srkColor.red(1), "%s %s" % (" [RSP - Info]: >>>  " + varWhs.slave,
                                                                    ' >>> Possible {},  in directory (302 - Redirect)'.format(
                                                                        varCkdir.raf.replace("/", ""))), srkColor.end())
                        else:
                            print("\t", srkColor.red(1), "%s %s %s" % (
                                " [RSP - Info]: >>>  " + varWhs.slave, " >>> Server Response:", response.status),
                                  srkColor.end())
                        connection.close()
                    print(" ")
                    print("\t", srkColor.bold(1), " [RSP - Info]: >>>  " + "Scan completed", srkColor.end())
                    print("")
                    print(srkColor.blue(1))
                    print(banner, srkColor.end())
                    print("")
                    print("")
                    print(srkColor.bold(1) + "\t", "=================================================" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|", '\t', '\t', ('Raport Scan'), "\t", "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|                                               |" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|                                               |" + srkColor.end())
                    print(srkColor.bold(1), "\t", "|", "\t", " Target pages found: ", varCkdir.shk, "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1), "\t", "|", "\t", " Raport pages scan:  ", varCkdir.pin, "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1) + "\t",
                          "|                                               | " + srkColor.end())
                    print(srkColor.bold(1) + "\t",
                          "|                                               | " + srkColor.end())
                    print(srkColor.bold(1) + "\t", "=================================================" + srkColor.end())
                    print(srkColor.bold(1))
                    input('         Press Enter to Exit')
                    print(srkColor.end())
                    exit()

                if varCkdir.opt == 4:
                    print(" ")
                    print("\t", ("[RSP - Info:] Scan: " + target))
                    print(" ")
                    for varCkdir.raf in varOpt_4:
                        varCkdir.raf = varCkdir.raf.replace("\n", "")
                        varCkdir.raf = "/" + varCkdir.raf
                        varWhs.slave = target + varCkdir.raf
                        print(srkColor.bold(1), ("[RSP - Scan]  " + varWhs.slave + "..."))
                        connection = http.client.HTTPConnection(target)
                        connection.request("GET", varCkdir.raf)
                        response = connection.getresponse()
                        varCkdir.pin = varCkdir.pin + 1
                        if response.status == 200:
                            varCkdir.shk = varCkdir.shk + 1
                            print(" ")
                            print("\t", srkColor.cyan(1),
                                  "%s %s" % (" [RSP - Info]: >>>  " + varWhs.slave, " >>> Target found!"),
                                  srkColor.end())
                            print(" ", srkColor.bold(1))
                            print("\t ", srkColor.bold(1), input("           Press 'Enter' to continue scanning."),
                                  srkColor.end())
                            print(" ", srkColor.end())
                        elif response.status == 404:
                            varCkdir.pin = varCkdir.pin
                        elif response.status == 302:
                            print("\t", srkColor.red(1), "%s %s" % (" [RSP - Info]: >>>  " + varWhs.slave,
                                                                    ' >>> Possible {},  in directory (302 - Redirect)'.format(
                                                                        varCkdir.raf.replace("/", ""))), srkColor.end())
                        else:
                            print("\t", srkColor.red(1), "%s %s %s" % (
                                " [RSP - Info]: >>>  " + varWhs.slave, " >>> Server Response:", response.status),
                                  srkColor.end())
                        connection.close()
                    print(" ")
                    print("\t", srkColor.bold(1), " [RSP - Info]: >>>  " + "Scan completed", srkColor.end())
                    print("")
                    print(srkColor.blue(1))
                    print(banner, srkColor.end())
                    print("")
                    print("")
                    print(srkColor.bold(1) + "\t", "=================================================" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|", '\t', '\t', ('Raport Scan'), "\t", "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|                                               |" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|                                               |" + srkColor.end())
                    print(srkColor.bold(1), "\t", "|", "\t", " Target pages found: ", varCkdir.shk, "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1), "\t", "|", "\t", " Raport pages scan:  ", varCkdir.pin, "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1) + "\t",
                          "|                                               | " + srkColor.end())
                    print(srkColor.bold(1) + "\t",
                          "|                                               | " + srkColor.end())
                    print(srkColor.bold(1) + "\t", "=================================================" + srkColor.end())
                    print(srkColor.bold(1))
                    input('         Press Enter to Exit')
                    print(srkColor.end())
                    exit()

                if varCkdir.opt == 5:
                    print(" ")
                    print("\t", ("[RSP - Info:] Scan: " + target))
                    print(" ")
                    for varCkdir.raf in varOpt_5:
                        varCkdir.raf = varCkdir.raf.replace("\n", "")
                        varCkdir.raf = "/" + varCkdir.raf
                        varWhs.slave = target + varCkdir.raf
                        print(srkColor.bold(1), ("[RSP - Scan]  " + varWhs.slave + "..."))
                        connection = http.client.HTTPConnection(target)
                        connection.request("GET", varCkdir.raf)
                        response = connection.getresponse()
                        varCkdir.pin = varCkdir.pin + 1
                        if response.status == 200:
                            varCkdir.shk = varCkdir.shk + 1
                            print(" ")
                            print("\t", srkColor.cyan(1),
                                  "%s %s" % (" [RSP - Info]: >>>  " + varWhs.slave, " >>> Target found!"),
                                  srkColor.end())
                            print(" ", srkColor.bold(1))
                            print("\t ", srkColor.bold(1), input("           Press 'Enter' to continue scanning."),
                                  srkColor.end())
                            print(" ", srkColor.end())
                        elif response.status == 404:
                            varCkdir.pin = varCkdir.pin
                        elif response.status == 302:
                            print("\t", srkColor.red(1), "%s %s" % (" [RSP - Info]: >>>  " + varWhs.slave,
                                                                    ' >>> Possible {},  in directory (302 - Redirect)'.format(
                                                                        varCkdir.raf.replace("/", ""))), srkColor.end())
                        else:
                            print("\t", srkColor.red(1), "%s %s %s" % (
                                " [RSP - Info]: >>>  " + varWhs.slave, " >>> Server Response:", response.status),
                                  srkColor.end())
                        connection.close()
                    print(" ")
                    print("\t", srkColor.bold(1), " [RSP - Info]: >>>  " + "Scan completed", srkColor.end())
                    print("")
                    print(srkColor.blue(1))
                    print(banner, srkColor.end())
                    print("")
                    print("")
                    print(srkColor.bold(1) + "\t", "=================================================" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|", '\t', '\t', ('Raport Scan'), "\t", "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|                                               |" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|                                               |" + srkColor.end())
                    print(srkColor.bold(1), "\t", "|", "\t", " Target pages found: ", varCkdir.shk, "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1), "\t", "|", "\t", " Raport pages scan:  ", varCkdir.pin, "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1) + "\t",
                          "|                                               | " + srkColor.end())
                    print(srkColor.bold(1) + "\t",
                          "|                                               | " + srkColor.end())
                    print(srkColor.bold(1) + "\t", "=================================================" + srkColor.end())
                    print(srkColor.bold(1))
                    input('         Press Enter to Exit')
                    print(srkColor.end())
                    exit()

                if varCkdir.opt == 6:
                    print(" ")
                    print("\t", ("[RSP - Info:] Scan: " + target))
                    print(" ")
                    for varCkdir.raf in varOpt_6:
                        varCkdir.raf = varCkdir.raf.replace("\n", "")
                        varCkdir.raf = "/" + varCkdir.raf
                        varWhs.slave = target + varCkdir.raf
                        print(srkColor.bold(1), ("[RSP - Scan]  " + varWhs.slave + "..."))
                        connection = http.client.HTTPConnection(target)
                        connection.request("GET", varCkdir.raf)
                        response = connection.getresponse()
                        varCkdir.pin = varCkdir.pin + 1
                        if response.status == 200:
                            varCkdir.shk = varCkdir.shk + 1
                            print(" ")
                            print("\t", srkColor.cyan(1),
                                  "%s %s" % (" [RSP - Info]: >>>  " + varWhs.slave, " >>> Target found!"),
                                  srkColor.end())
                            print(" ", srkColor.bold(1))
                            print("\t ", srkColor.bold(1), input("           Press 'Enter' to continue scanning."),
                                  srkColor.end())
                            print(" ", srkColor.end())
                        elif response.status == 404:
                            varCkdir.pin = varCkdir.pin
                        elif response.status == 302:
                            print("\t", srkColor.red(1), "%s %s" % (" [RSP - Info]: >>>  " + varWhs.slave,
                                                                    ' >>> Possible {},  in directory (302 - Redirect)'.format(
                                                                        varCkdir.raf.replace("/", ""))), srkColor.end())
                        else:
                            print("\t", srkColor.red(1), "%s %s %s" % (
                                " [RSP - Info]: >>>  " + varWhs.slave, " >>> Server Response:", response.status),
                                  srkColor.end())
                        connection.close()
                    print(" ")
                    print("\t", srkColor.bold(1), " [RSP - Info]: >>>  " + "Scan completed", srkColor.end())
                    print("")
                    print(srkColor.blue(1))
                    print(banner, srkColor.end())
                    print("")
                    print("")
                    print(srkColor.bold(1) + "\t", "=================================================" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|", '\t', '\t', ('Raport Scan'), "\t", "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|                                               |" + srkColor.end())
                    print(srkColor.bold(1) + "\t", "|                                               |" + srkColor.end())
                    print(srkColor.bold(1), "\t", "|", "\t", " Target pages found: ", varCkdir.shk, "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1), "\t", "|", "\t", " Raport pages scan:  ", varCkdir.pin, "\t", "\t", "|",
                          "\t" + srkColor.end())
                    print(srkColor.bold(1) + "\t",
                          "|                                               | " + srkColor.end())
                    print(srkColor.bold(1) + "\t",
                          "|                                               | " + srkColor.end())
                    print(srkColor.bold(1) + "\t", "=================================================" + srkColor.end())
                    print(srkColor.bold(1))
                    input('         Press Enter to Exit')
                    print(srkColor.end())
                    exit()

            except (KeyboardInterrupt, SystemExit):
                print("\t", srkColor.bold(1), "[RSP - Info:] Session exit", srkColor.end())

            except socket.error:
                print(" ")
                print("\t", srkColor.bold(1), "[RSP - Info]", "Is not - valid Url !!", srkColor.end())
                print("\t", srkColor.bold(1), "[RSP - Info]", "Insert target  without ('/') - e.g http://site.com")
                print(" ")
                input('         Press Enter to Exit')
                print(" ")

        if varStorm.menu == "+":
            varStorm.menuChoice2 = input("          Enter the list file name  .e.g [list.txt]: ")
            open_list = open(varStorm.menuChoice2).readlines()
            for line in open_list:
                if "?" in line:
                    links = line.strip()
                    target = links
                    print(srkColor.bold(1), "[RSP - Scan]: >>> Audit Snippet >>> Scan List[n/t]")
                    sharky_rce_test_full(target)
                    sharky_xxs_test_full(target)
                    sharky_sqli_test_full(target)
                    sharky_waf_test_full(target)
                else:
                    links = line.strip()
                    target = links
                    print(srkColor.bold(1))
                    print([RSP - Info], "Is not a valid Url !!", srkColor.end())
                    print([RSP - Info], "You should write target - e.g http://site.com/page.php?id=value")
                    print(" ")
                    input('         Press Enter to Exit')
                    print(srkColor.end())
            exit()

except (RuntimeError, TypeError, NameError):
    print(srkColor.bold(1))
    print("\t", "[RSP -Info]", "There is something wrong !")
    print(" ")
    print("\t", "[RSP -Info]", "Insert valid URL")
    print("\t", "[RSP - Info]", "You should write target - e.g http://site.com/page.php?id=value")
    print(" ")
    input('         Press Enter to Exit')
    print(" ")
    print(srkColor.bold(1), "[RSP - Info:] Session exit", srkColor.end())
    print(srkColor.end())
except (KeyboardInterrupt, SystemExit):
    print("\t", srkColor.bold(1), "[RSP - Info:] Session exit", srkColor.end())
    exit()
