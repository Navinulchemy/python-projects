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

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

rev_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rev_alpha.reverse()
#cipher_text = ""#declaring variables globally outside the function will print the result with the previous output
#normal_text = ""#declaring variables globally outside the function will print the result with the previous output


def encode(characters, shift):
    cipher_text=""
    for letters in characters:
        #global cipher_text ---->   #by declaring a var global we can alter, modify a var
        if letters in alphabet:
            find = alphabet.index(letters)
            new = find + shift
            cipher_text += alphabet[new]
        else:
            cipher_text += letters
    print(f"The Encoded text is  {cipher_text}")


def decode(characters,shift):
    normal_text = ""
    for letters in characters:
        #global normal_text---->   #by declaring a var global we can alter, modify a var
        if letters in rev_alpha:
            find = rev_alpha.index(letters)
            new = find + shift
            normal_text += rev_alpha[new]
        else:
          normal_text += letters
    print(f"The Decoded text is  {normal_text}")


print(logo)
flag = True
while flag == True:
    choice = input("Want to encode or decode type your choice : ").lower()
    print("Shift range must between 1 to 25")
    characters = input("Enter your characters : ").lower()
    shift = int(input("Enter your shift range in whole number : "))
    if shift > 25:
        print("shift amount must between 1 - 25")
        shift = (int(input("Enter your shift range again : ")))

    if "encode" in choice:
        encode(characters, shift)
    elif "decode" in choice:
        decode(characters, shift)

    wish = int(input("Enter 0 to proceed or Enter 1 to quit :"))
    if wish == 0:
        flag = True
    else:
        flag = False
