import hashlib

def hash_password(password):
    pass_bytes=password.encode('utf-8')
    hash_object=hashlib.sha256(pass_bytes)
    pass_hash=hash_object.hexdigest()
    return pass_hash

password=input("enter password : ")
hashed_password=hash_password(password)
print(f"Your hashed password is : {hashed_password}")   
