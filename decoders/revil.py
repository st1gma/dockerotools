import sys
import pefile
import string
import struct
import json
from Crypto.Cipher import ARC4

'''
Juan Figuera
2020-01-09
Revil/Sodinokibi Config Extractor
'''

def extract_revil_config(filename):
    printable = set(string.printable)
    pe = pefile.PE(filename)
    section = pe.sections[3]
    data = section.get_data()
    length = struct.unpack('I', data[0x24:0x28])[0]
    decoded = ''.join(filter(lambda x: x in string.printable, str(ARC4.new(data[0:32]).decrypt(data[0x28:length + 0x28]), 'utf-8')))
    parsed_config = json.loads(decoded.strip())
    return parsed_config

if __name__ == "__main__":
    print(json.dumps(extract_revil_config(sys.argv[1]), indent=2, sort_keys=True))