import re

def check(password):
    length_regex=re.compile(r'^.{8,}$')
    upper_regex=re.compile(r'[A-Z]')
    lower_regex=re.compile(r'[a-z]')
    special_regex=re.compile(r'[\w_]')
    digit_regex=re.compile(r'\d')

    length_check=length_regex.search(password)
    upper_check=upper_regex.search(password)
    lower_check=lower_regex.search(password)
    special_check=special_regex.search(password)
    digit_check=digit_regex.search(password)

    if length_check and upper_check and lower_check and special_check and digit_check:
        return True
    else:
        return False
    

with open('pass.txt') as p:
    for password in p:
        password=password.strip()
        if check(password):
            print("Valid password : ",password)
        else:
            print("Invalid password : ",password)