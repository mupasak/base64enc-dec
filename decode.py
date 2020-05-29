#!/usr/bin/python3
import base64 

passwd = "Q2hpbiBVcCBSb2Nrc3RhcnQ="
dec = passwd.encode('ascii')
message = base64.b64decode(dec)
final = message.decode('ascii')
print (final)
