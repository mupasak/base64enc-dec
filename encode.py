#!/usr/bin/python3

import base64 

enc_str = 'Chin up rockstar'
enc = enc_str.encode('ascii')
msg = base64.b64encode(enc)
final = msg.decode('ascii')
print (final)
