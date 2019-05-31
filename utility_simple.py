#!/usr/bin/python3
import codecs
import sys

def convertHexToBase64(hexVal):
    """Takes a Hexadecimal string as input and returns a Base64 string. Requires proper hex string with no 0x prefix and even length"""
    hexVal = codecs.decode(hexVal, 'hex')
    return codecs.encode(hexVal, 'base64').strip()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid command line usage. Please try: python {} <hex-string>".format(sys.argv[0]))
        sys.exit(1)
    print(convertHexToBase64(sys.argv[1]))
