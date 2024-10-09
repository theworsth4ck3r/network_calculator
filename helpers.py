import sys

__INVALID_IP_ADDRESS_ERROR_MESSAGE = 'IP Address is invalid'


def validateIpAddress(ipAddress):
    octs = ipAddress.split(".")
    if len(octs) != 4:
        print(__INVALID_IP_ADDRESS_ERROR_MESSAGE)
        sys.exit(1)
        
    for singleOct in octs:
        try:
            intSingleOct = int(singleOct)
            if intSingleOct < 0 or intSingleOct > 255:
                print(__INVALID_IP_ADDRESS_ERROR_MESSAGE)
                sys.exit(1)
        except ValueError:
            print(__INVALID_IP_ADDRESS_ERROR_MESSAGE)
            sys.exit(1)
        except Exception:
            print('An unknown error')
            sys.exit(1)    
    

# Crates given amount of bits
# Example: 8 -> 1, 2, 4, 8, 16, 32, 64, 128
def getBits(amountBitsToCreate):
	arr = []

	for x in range(0, amountBitsToCreate):
		arr.append(pow(2, x))

	return arr[::-1]


# Converts subnet mask given as string to binary number
def getSubnetMaskBin():
	return ipToBin(sys.argv[2])


# Takes IP as a string and converts it to decimal number
def ipToDec(ipAddress):
	ipBinArr = []
	bits = getBits(8)

	octs = [
		ipAddress[0:8],
		ipAddress[8:16],
		ipAddress[16:24],
		ipAddress[24:32]
	]

	for octsIndex in range(0, len(octs)):
		octBin = 0
		for singleBinIndex in range(0, len(octs[octsIndex])):
			if int(octs[octsIndex][singleBinIndex]) == 1:
				octBin += int(bits[singleBinIndex])

		ipBinArr.append(octBin)
		octBin = 0

	return '.'.join(str(x) for x in ipBinArr)


# Takes ip address as a string and converts it to binary number
def ipToBin(ipAddress):
	octs = ipAddress.split('.')

	bits = getBits(8)
	binIpArr = []

	for index in range(0, len(octs)):
		octBin = ""
		total = 0

		for bitIndex in range(0, len(bits)):
			if int(octs[index]) >= (bits[bitIndex] + total):
				total += int(bits[bitIndex])
				octBin += str(1)
			else:
				octBin += str(0)

		binIpArr.append(octBin)


	return ''.join(str(x) for x in binIpArr)
