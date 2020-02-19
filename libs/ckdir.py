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



class ckdirSec:
    def __init__(self, apache, asp_net, node_js, cfm_server, cgi_server, brf_server ):
        self.apache = apache
        self.asp_net = asp_net
        self.node_js = node_js
        self.cfm_server = cfm_server
        self.cgi_server = cgi_server
        self.brf_server = brf_server

varCkd = ckdirSec('apache_format', 'asp_net_format', 'nodejs_format', 'cfm_format', 'cgi_format', 'brf_format')

varCkd.apache = open("libs/rSec/_ckdir/_apache.txt", "r").readlines()
varOpt_1 = varCkd.apache

varCkd.asp_net = open("libs/rSec/_ckdir/_asp_net.txt", "r").readlines()
varOpt_2 = varCkd.asp_net

varCkd.node_js = open("libs/rSec/_ckdir/_node_js.txt", "r").readlines()
varOpt_3 = varCkd.node_js

varCkd.cfm_server = open("libs/rSec/_ckdir/_cfm.txt", "r").readlines()
varOpt_4 = varCkd.cfm_server

varCkd.cgi_server = open("libs/rSec/_ckdir/_cgi.txt", "r").readlines()
varOpt_5 = varCkd.cgi_server

varCkd.brf_server = open("libs/rSec/_ckdir/_brf.txt", "r").readlines()
varOpt_6 = varCkd.brf_server
