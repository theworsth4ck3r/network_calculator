# theworsth4ck3r
# 2019-07-06

import sys
from helpers import ipToBin, ipToDec, getSubnetMaskBin, validateIpAddress

if len(sys.argv) != 3:
	print("Provide IP address of device and subnet mask address.\nExample: 192.168.1.234 255.255.255.0")
	sys.exit(1)
 

validateIpAddress(sys.argv[1])
validateIpAddress(sys.argv[2])


_NetworkAddress = ''
_BroadcastAddress = ''
_MaxiumumHosts = ''
_FirstHostIP= ''
_LastHostIP = ''


def calcNetworkAddress():
	global _NetworkAddress

	ip_address_bin = ipToBin(sys.argv[1])
	subnet_mask_bin = ipToBin(sys.argv[2])
	# print(ip_address_bin)
	if len(ip_address_bin) != 32:
		print("Binary ip address doesn't have 32 bits")
		exit(1)


	network_address_bin = ''
	for x in range(0, 32):
		network_address_bin += str(int(ip_address_bin[x]) * int(subnet_mask_bin[x]))

	_NetworkAddress = ipToDec(network_address_bin)


def calcBroadcastAddress():
	global _NetworkAddress
	global _BroadcastAddress

	subnetmask_bin = getSubnetMaskBin()
	subnetmask_reversed_bin = ''

	for x in range(0, len(subnetmask_bin)):
		if int(subnetmask_bin[x]) == 1:
			subnetmask_reversed_bin += '0'
		else:
			subnetmask_reversed_bin += '1'
	

	subnetmask_reversed_dec = ipToDec(subnetmask_reversed_bin)

	subnetmask_reversed_dec_arr = subnetmask_reversed_dec.split('.')
	network_address_arr = _NetworkAddress.split('.')

	broadcast_address_arr = []
	for index in range(0, 4):
		broadcast_address_arr.append(
			str(int(subnetmask_reversed_dec_arr[index]) + int(network_address_arr[index]))
			)

	_BroadcastAddress = '.'.join(str(x) for x in broadcast_address_arr)
		

def getMaximumHostsAmount():
	global _MaxiumumHosts

	subnetmask_short = 0
	subnetmask_bin = getSubnetMaskBin()

	for x in range(0, len(subnetmask_bin)):
		if int(subnetmask_bin[x]) == 1:
			subnetmask_short += 1

	_MaxiumumHosts = pow(2, 32 - subnetmask_short) - 2


def getFirstHostIP():
	global _NetworkAddress
	global _FirstHostIP

	network_address_arr = _NetworkAddress.split('.')
	network_address_arr[3] = str(int(network_address_arr[3]) + 1)

	_FirstHostIP = '.'.join(str(x) for x in network_address_arr)


def getLastHostIP():
	global _BroadcastAddress
	global _LastHostIP

	broadcast_address_arr = _BroadcastAddress.split('.')
	broadcast_address_arr[3] = str(int(broadcast_address_arr[3]) - 1)

	_LastHostIP = '.'.join(str(x) for x in broadcast_address_arr)


calcNetworkAddress()
calcBroadcastAddress()
getMaximumHostsAmount()
getFirstHostIP()
getLastHostIP()

print('''

------------------------------------
Network address      %s
Broadcast address    %s
Maximum hosts        %d
First host IP        %s
Last host IP         %s
------------------------------------
''' % (_NetworkAddress, _BroadcastAddress, _MaxiumumHosts, _FirstHostIP, _LastHostIP))


