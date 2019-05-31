#!/usr/bin/python3
import codecs
import sys
import unittest


def convertHexToBase64(hexVal):
    """Takes a Hexadecimal string as input and returns a Base64 string"""
    try:
        int(hexVal, 16)
    except ValueError:
        raise ValueError("The provided string '{}' is not a valid Hexadecimal string.".format(hexVal))

    # if the hex string is prefixed with '0x' strip it off
    if len(hexVal) > 2:
        if hexVal[:2].lower() == '0x':
            hexVal = hexVal[2:]

    # ensure the hexVal parameter is even in length prior to converting the string to hex
    if len(hexVal) % 2 != 0:
        hexVal = '0' + hexVal

    hexVal = codecs.decode(hexVal, 'hex')
    return codecs.encode(hexVal, 'base64').strip()


class TestHexToBase64Conversion(unittest.TestCase):

    def test_noPrefix(self):
        hexString = '45766964696e74'
        expectedBase64 = 'RXZpZGludA=='
        self.assertEqual(convertHexToBase64(hexString), expectedBase64)

    def test_prefix(self):
        hexString = '45766964696e74'
        expectedBase64 = 'RXZpZGludA=='
        self.assertEqual(convertHexToBase64('0x'+hexString), expectedBase64)

    def test_invalidHexString(self):
        invalidHex = 'hello'
        with self.assertRaises(ValueError):
            convertHexToBase64(invalidHex)

    def test_oddLength(self):
        hexString = 'abcde'
        expectedBase64 = 'Crze'
        self.assertEqual(convertHexToBase64(hexString), expectedBase64)

    def test_oddLength_prefix(self):
        hexString = '0xabcde'
        expectedBase64 = 'Crze'
        self.assertEqual(convertHexToBase64(hexString), expectedBase64)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid command line usage. Please try: python {} <hex-string>".format(sys.argv[0]))
        sys.exit(1)
    print(convertHexToBase64(sys.argv[1]))
