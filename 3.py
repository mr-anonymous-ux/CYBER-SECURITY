import re

def validate(password):
    if len(password)<8:
       return False
    
    if not  re.search(r'[A-Z]',password):
        return False
    
    if not re.search(r'[a-z]',password):
        return False
    
    if not re.search(r'\d',password):
        return False
    
    if not re.search(r'[!@#$%^&*()_+<>?{}|:"]',password):
        return False
    
    return True

password=input("enter password : ")
is_valid=validate(password)
if is_valid:
    print("valid password")
else:
    print("Invalid password")