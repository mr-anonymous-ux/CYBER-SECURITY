import requests
import hashlib

with open('6pass.txt','r') as f:
    for line in f:
        username,password=line.strip().split(',')

        password_hash=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        response=requests.get(f"https://api.pwnedpasswords.com/range/{password_hash[:5]}")

        if response.status_code==200:
            hashes=[line.split(':') for line in response.text.splitlines()]

        for h,count in hashes:
            if password_hash[5:]==h:
                print(f"Password for {username} has been leaked {count} times")
                break
            else:
                print(f"could not check password for {username}")
        else:
            print(f"could not check password for {username}")
