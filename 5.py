import re

def strength(password):
    suggestions=[]
    score=0

    if len(password)>=8:
        score+=1
    else:
        suggestions.append("Password should be atleast 8 characters long")

    if re.search(r'[A-Z]',password):
        score+=1
    else:
        suggestions.append("Password should have atleast 1 uppercase letter")

    if re.search(r'[a-z]',password):
        score+=1
    else:
        suggestions.append("Password should have atleast 1 lowercase letter")

    if re.search(r'\d',password):
        score+=1
    else:
        suggestions.append("Password should have atleast 1 numeric digit")

    if re.search(r'[!@#$%^&*()_+{}:"|<>?]',password):
        score+=1
    else:
        suggestions.append("Password should have atleast 1 specialcase letter")

    return score,suggestions

password=input("enter password : ")
print(strength(password))
