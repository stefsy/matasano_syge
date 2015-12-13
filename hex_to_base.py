
# Hex16  (0 - 9, A - F)
# Base64 (A-Z, a-z, 0-9, +, /)

from codecs import decode

def hex2base_using_decode(hexval):
	'''
	decoding from hex, then encoding to base64
	test against this function
	'''
	hexstr = tstr.decode(encoding='hex', errors='strict')
	return hexstr.encode(encoding='base64', errors='strict')

def hex2base(hexval):
	''' placeholder ''' 
	for char in hexval: 
		print ord(char)
	pass


if __name__ == '__main__':
	str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
	print hex2base_using_decode(tstr)