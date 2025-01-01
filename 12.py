from cryptography.fernet import Fernet
key=Fernet.generate_key()
f=Fernet(key)
token=f.encrypt(b"welconme to cyber security lab")

print(token)

d=f.decrypt(token)
print(d)