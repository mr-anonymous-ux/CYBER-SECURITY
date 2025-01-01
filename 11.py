import base64

str1=input("enter text : ")
byte1=str1.encode('ascii')
byte2=base64.b64encode(byte1)

print("encoded string is : ",byte2)

decoded_byte=base64.b64decode(byte2)
decoded_string=decoded_byte.decode('ascii')

print("decoded string is : ",decoded_string)