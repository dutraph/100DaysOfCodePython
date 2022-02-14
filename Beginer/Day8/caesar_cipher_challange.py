alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w',
            'v', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


def caesar(plain_text, shift_number, cipher_type):
    cipher_text = ""
    if cipher_type == 2:
        shift_number *= -1
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_number
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    return cipher_text


def start():
    print(logo)
    direction = int(input("Type 1=encode to encrypt, type 2=decode to decrypt:\n"))
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 54:
        shift %= 26
    msg_encoded = caesar(text, shift, direction)
    if direction == 1:
        print(f"Encrypted Message = {msg_encoded}")
    else:
        print(f"Decrypted Message = {msg_encoded}")
    replay = input("e=exit / r=re-run: ")
    if replay == "r":
        start()
    else:
        print("Bye...")


start()
