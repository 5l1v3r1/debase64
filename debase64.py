#!usr/bin/python
#By virus baghdad
#For Encode And Decode Base64




from termcolor import colored
import base64
print colored ('''
        +=======================================+
        |................Base64.................|
        +---------------------------------------+
        |............. virus baghdad ...........|
        +---------------------------------------+
: www.facebook.com/virus.baghdad.0
''', 'red')

y= input("hash:")

M=base64.b64encode(y)
N=base64.b64decode(y)
x=input('''
1- to encrypt texts
2- to decrypt 
>>>>: ''')
if x == 1:
 print ("Encryption:" + (M) )
elif x == 2:
 print ("Successfully decryption: " + (N) )
print  colored ('''
           +========================================+
           |   Thank you can follow us on Facebook  |
           +========================================|
           |https://www.facebook.com/virus.baghdad.0|
           +========================================+
press enter for exit:''', 'red')
raw_input(":")


