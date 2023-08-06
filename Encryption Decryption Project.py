#!/usr/bin/env python
# coding: utf-8

# In[1]:


def encrypt(text, shift):
    cipher_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            cipher_text += encrypted_char
        else:
            cipher_text += char
    return cipher_text


def decrypt(cipher_text, shift):
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


# Taking user input
input_text = input("Enter the text to encrypt: ")
shift_amount = int(input("Enter the shift amount (0-25): "))

# Encrypt the input text
encrypted_text = encrypt(input_text, shift_amount)
print("Encrypted text:", encrypted_text)

decrypt_choice = input("Do you want to decrypt the text? (yes/no): ")

if decrypt_choice.lower() == "yes":
    decryption_shift = int(input("Enter the shift amount for decryption: "))
    if decryption_shift == shift_amount:
        decrypted_text = decrypt(encrypted_text, decryption_shift)
        print("Decrypted text:", decrypted_text)
    else:
        print("Error: Invalid shift amount for decryption. Decryption failed.")


# In[ ]:




