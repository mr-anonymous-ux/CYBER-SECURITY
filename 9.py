print("enter the caesar cipher text : ")
message=input(">")

for shift in range(26):
    result=""

    for char in message:
        if char.isalpha():
            ascii_offset=ord('A')if char.isupper() else ord('a')
            char=chr((ord(char)-ascii_offset-shift)%26+ascii_offset)

        result+=char

    print(f"Key : {shift}|Decrypted message : {result}")