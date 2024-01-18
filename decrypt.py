from letters import alphabet

message = input("Enter the message you would like to decrypt => ")
shift = int(input("Type the shift number => "))
shift = shift%26

def caesar_cipher_decryption(message , shift):
    letter = []
    cipher_text  = ""

    for index in message:
        letter.append(index)

   
    for v in range(len(letter)):
        if letter[v] in alphabet:
            position = alphabet.index(letter[v])
            new_position = position - int(shift) % 26

            if(new_position >= 26):
                new_position = new_position -26
           
            cipher_text += alphabet[new_position]
            
        else:
            cipher_text += letter[v]
            

    print(f"The decrypted message is : {cipher_text}")


caesar_cipher_decryption(message , shift)