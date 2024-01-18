from letters import alphabet
import random

message = input("Enter the message you would like to encrypt => ")
shift = random.randint(0, 1000000000000000)

shift = shift%26

def caesar_cipher_encryption(message , shift):
    letter = []
    cipher_text  = ""

    for index in message:
        letter.append(index)

   
    for v in range(len(letter)):
        if letter[v] in alphabet:
            position = alphabet.index(letter[v])
            new_position = position + int(shift) % 26

            if(new_position >= 26):
                new_position = new_position -26
           
            cipher_text += alphabet[new_position]
            
        else:
            cipher_text += letter[v]
            

    print(f"The encrypted message is : {cipher_text} \nThe number used to encrypt the message is {shift}")


caesar_cipher_encryption(message , shift)