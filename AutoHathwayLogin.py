'''
	Copyright (C) 2013 Sameer Balasubrahmanyam
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 '''
import urllib2, sys, time, socket, sh

userName="yourID"
password="YorPSW"

sleepTime=3600
socket.setdefaulttimeout(sleepTime)

hostname = [ '203.212.193.60']
url = "/bsp/login.do?action=doLoginSubmit&flowId=UserLogin&username=" + userName + "&password=" + password

file=None
if file is None:
	#try:
	fh = open("hathway.log", 'w')
	#except IOError:
	#	print "Couldn't write to file /tmp/hathway.log";
else:
	try:
		fh = open(file, 'w')
	except IOError:
		print "Couldn't write to file %s\n" % (file);

	
def local_write(str):
	sys.stdout.write(str)
	fh.write(str)
	fh.flush()

def checkInternetConnectivity():
	x = 1
	try:
		sh.ping("www.google.com", "-c 1", _out="/dev/null")
		#socket.create_connection( ("www.google.com", 80) )
	except sh.ErrorReturnCode_1:
		x = 0
	finally:
		return x

def connectToHathway():

	if len(hostname) == 0:
		sys.exit(1)
	else:
		for host in hostname:
			real_host = "http://" + host + url
			try:
				local_write("%s\tTrying to authenticate to server %s\n" % (time.ctime(), real_host) )
				urllib2.urlopen(real_host)
			except:
				local_write("%s\tFailed to connect to %s Retrying\n" % (time.ctime(), real_host) )
				continue
	

while 1==1:
	if checkInternetConnectivity() == 0:
		local_write("%s\tInternet connectivity is dead. Trying to contact Hathway auth severs.\n" % (time.ctime() ) )
		connectToHathway()
		time.sleep(sleepTime)
		continue
	else:
		local_write("%s\tInternet connectivity alive. Sleeping for %s seconds.\n" % (time.ctime(), sleepTime) )
		time.sleep(sleepTime)
		continue 


