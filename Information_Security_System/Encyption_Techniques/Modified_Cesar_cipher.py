# encryption
def encryptCesarCipher(text, k):
    temp = ""
    for char in text: #accessing each character one by one
        i = ord(char) #converting character into its ascii value using ord() method
        if (i >= 97 and i <= 122):
            temp += chr((i+k-97) % 26+97) #adding key to the ascii value and keeping it in range of ascii value of alphabets for (a-z). Then converting it back to character using chr() method
        elif (i >= 65 and i <= 90):
            temp += chr((i+k-65) % 26+65) #adding key to the ascii value and keeping it in range of ascii value of alphabets for (A-Z). Then converting it back to character using chr() method
        else:
            temp += char #adding special character as it is(eg: spaces, $, # etc.)
    return temp #returning the ciphertext string

# decryption
def decryptCesarCipher(cText, k):
    temp = ""
    for char in cText:
        i = ord(char) #converting character into its ascii value
        if (i >= 97 and i <= 122):
            temp += chr((i+k-97) % 26+97) #converting it back to original character, the main part here is how we handle the key before passing it to the function
        elif (i >= 65 and i <= 90):
            temp += chr((i+k-65) % 26+65) #converting it back to original character, the main part here is how we handle the key before passing it to the function
        else:
            temp += char
    return temp


# Menu options
print('''Welcome to Cesar Cipher Executor:
This program will help you to encrypte as well as decrypte your messages using cesar cipher technique.
 Choose the operation you want to perform:-
    -> Press 1 for Encryption of your message
    -> Press 2 for Decryption of your message
    -> Press Any other key to exit the program

NOTE!!!!! Do have your key ready with you because without it, this software is of no use.''')
cipherText = None
m = int(input("Select the Operation to Perform: "))
while (True): #Infinite loop
    if (m == 1):
        plaintext = input("Enter your message: ")
        key = int(input("Enter your secret key (between = 1 - 25) : "))
        cipherText = encryptCesarCipher(plaintext, key % 25) #applied check for keeping the key under the range
        print(cipherText)
    elif (m == 2):
        if (cipherText != None):
            print('''Do you want to use the Cipher-Text you have encypted in previous step?
            -> Press 1 to use that
            -> Press any other key to Enter some other Cipher-Text''')
            n = int(input("Enter choice: "))
            if (n != 1):
                cipherText = input("Enter your message: ")
        else:
            cipherText = input("Enter your message: ")
        key = int(input("Enter your secret key (between = 1 - 25) : "))
        originalText = decryptCesarCipher(cipherText, 26-(key % 25)) #the main part of decryption is here:
        # -> first we check that key is in range
        # -> then we subtract the key from the total alphabets available(i.e. we have subtracted the key from the total number of shift available to us for encyption)
        # NOTE: unlike in the encryption process here we are subtracting key from the total alphabets available to us due to the concept of keeping the character in the specific range(like a circle 97 to 122 or 65 to 90)
        print(originalText)
    else:
        print("Thanks for Using this Program :)")
        exit() #exiting the program
    print('''----------------------------------------------------------------
Choose the operation you want to perform:-
    -> Press 1 for Encryption of your message
    -> Press 2 for Decryption of your message
    -> Press Any other key to exit the program
    ''')
    m = int(input("Select the Next Operation to Perform(To exit press any key): "))
