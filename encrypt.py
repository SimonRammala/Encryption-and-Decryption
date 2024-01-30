from characters import alphabet, special_characters  # Importing the 'alphabet' and 'special characters' list from the 'characters' module
import random  # Importing the 'random' module for generating random numbers

# Asking the user for a message to encrypt
message = input("Enter the message you would like to encrypt => ").upper()

# Generating a random shift value
shift = random.randint(0, 1000000000000000)
shift = shift % 26  # Ensuring the shift value is within the range of the alphabet



# Function to perform Caesar cipher encryption
def caesar_cipher_encryption(message, shift):
    letter = []  # Empty list to store individual characters of the message
    cipher_text = ""  # Variable to store the encrypted message

    # Splitting the message into individual characters and storing them in the 'letter' list
    for index in message:
        letter.append(index)

    # Iterating through each character in the message
    for v in range(len(letter)):
        # Selecting a random character from the list
        random_character = random.choice(special_characters)

        if letter[v] in alphabet:  # Checking if the character is in the alphabet
            position = alphabet.index(letter[v])  # Finding the position of the character in the alphabet
            new_position = position + int(shift) % 26  # Calculating the new position after shifting

            if new_position >= 26:  # If the new position exceeds the alphabet length, wrap around
                new_position = new_position - 26

            cipher_text += alphabet[new_position]  # Appending the encrypted character to the cipher text
        else:
            cipher_text += random_character  # If the character is not in the alphabet, append it as it is to the cipher text

    # Printing the encrypted message and the shift used for encryption
    print(f"The encrypted message is: {cipher_text}\nThe number used to encrypt the message is {shift}")


# Calling the encryption function with the provided message and shift
caesar_cipher_encryption(message, shift)