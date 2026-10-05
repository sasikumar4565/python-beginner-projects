import random
import string

print("===== PASSWORD GENERATOR =====")

length = 12

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Password length:", length)
print("Generated Password:", password)
