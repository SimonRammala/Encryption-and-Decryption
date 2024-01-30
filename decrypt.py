from characters import alphabet, special_characters  # Importing the 'alphabet' list from the 'letters' module

# Asking the user for a message to decrypt
message = input("Enter the message you would like to decrypt => ").upper()

# Asking the user for the shift number
shift = int(input("Type the shift number => "))
shift = shift % 26  # Ensuring the shift value is within the range of the alphabet

# Function to perform Caesar cipher decryption
def caesar_cipher_decryption(message, shift):
    letter = []  # Empty list to store individual characters of the message
    decrypted_text = ""  # Variable to store the decrypted message

    # Splitting the message into individual characters and storing them in the 'letter' list
    for index in message:
        letter.append(index)

    # Iterating through each character in the message
    for v in range(len(letter)):
        if letter[v] in alphabet:  # Checking if the character is in the alphabet
            position = alphabet.index(letter[v])  # Finding the position of the character in the alphabet
            new_position = position - int(shift) % 26  # Calculating the new position after shifting back

            if new_position < 0:  # If the new position is negative, wrap around
                new_position = new_position + 26

            decrypted_text += alphabet[new_position]  # Appending the decrypted character to the decrypted text
        else:
            decrypted_text += " "  # If the character is not in the alphabet, append it as it is to the decrypted text

    # Printing the decrypted message
    print(f"The decrypted message is: {decrypted_text}")


# Calling the decryption function with the provided message and shift
caesar_cipher_decryption(message, shift)