import itertools
import string

def brute(password):
    chars=string.printable.strip()
    attempts=0

    for length in range(1,len(password)+1):
        for guess in itertools.product(chars,repeat=length):
            attempts+=1
            guess=''.join(guess)

            if guess==password:
               return(attempts,guess)
        
    return(attempts,None)

password=input("Enter password : ")
attempts,guess=brute(password)

if guess:
    print(f"Password cracked in {attempts} attempts.the password is {guess}")
else:
    print(f"Password not cracked in {attempts} attempts")