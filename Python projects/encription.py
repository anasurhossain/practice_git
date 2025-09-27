# import
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters 
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars : {chars}")
#print(f"key : {key}")

#Encrypt

plain_text = input("Enter your text here : ")
cipher_text = ""

for letters in plain_text:
    index = chars.index(letters)
    cipher_text += key[index]

print(f"Original Massage : {plain_text}")
print(f"Cipher Massage : {cipher_text}")

#Decrypt

cipher_text = input("Enter your Massage : ")
plain_text = ""

for letters in cipher_text:
    index = key.index(letters)
    plain_text += chars[index]

print(f"Encripted Massage : {cipher_text}")
print(f"Original Massage : {plain_text}")
