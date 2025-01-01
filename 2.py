import string
import random

def generate_pass(length=8):
    all_char=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(all_char) for i in range(length))
    return password

pass_length_str=input("enter the length of password : ")
if pass_length_str:
    pass_length=int(pass_length_str)
else:
    pass_length=8

password=generate_pass(pass_length)
print(f"The genrated password is {password}")