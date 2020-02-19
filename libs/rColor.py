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



class rspPalette:
	def red(self, num):
		return (("\033[%d;31m" % (int(num))))

	def end(self):
		return (("\033[0m"))

	def white(self, num):
		return (("\033[%d;38m" % (int(num))))

	def green(self, num):
		return (("\033[%d;32m" % (int(num))))

	def yellow(self, num):
		return (("\033[%d;33m" % (int(num))))

	def blue(self, num):
		return (("\033[%d;34m" % (int(num))))

	def cyan(self, num):
		return (("\033[%d;36m" % (int(num))))

	def purple(self, num):
		return (("\033[%d;35m" % (int(num))))

	def bold(self, num):
		return (("\033[%d;1m" % (int(num))))

	def uline(self, num):
		return (("\033[%d;4m " % (int(num))))

srkColor = rspPalette()