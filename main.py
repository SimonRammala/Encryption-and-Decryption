from art import *  # Importing the 'art' module for ASCII art
import subprocess  # Importing the 'subprocess' module for executing external commands

# A welcome message to the user
greetings = "Welcome to the realm of text \n message encryption and decryption."
tprint(greetings)  


print("==============================================================================================================================================================================================")

# Initializing the choice variable to 'yes' to enter the loop
choice = 'yes'

# Loop to continue the program until the user decides to exit
while(choice == 'yes'):

    # Asking the user to choose between encryption or decryption
    option = input("Type 'encode' to encrypt or type 'decode' to decrypt =>").lower()

    # Checking the user's choice
    if(option == 'encode'): 
        subprocess.call(['python3', 'encrypt.py'])  # Calling the encryption script using subprocess
    elif(option == 'decode'):  
        subprocess.call(['python3', 'decrypt.py'])  # Calling the decryption script using subprocess
    else:  
        print("You have entered an invalid option. Please try again.")

    # Asking the user if they want to continue
    choice = input("Would you like to continue? Type 'YES' or 'NO' => ").lower()

# A farewell message to the user
goodbye = "Thank you for using my service."
tprint(goodbye)  