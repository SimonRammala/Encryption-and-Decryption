from letters import alphabet

message = input("Enter your message => ")
shift = int(input("Type the shift number => "))
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
            cipher_text += alphabet[new_position]
        else:
            cipher_text +=letter[v]
            

    print(f"The encoded text is {cipher_text}")






caesar_cipher_encryption(message , shift)

