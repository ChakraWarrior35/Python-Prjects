# it's a password generation automatically generate a strong password

import random
import string

def pass_gen(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()-+"

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    all_chars = lowercase + uppercase + digits + special_chars
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return ''.join(password)
if __name__ == "__main__":
    print("Generated Password:", end=" ")
    print(pass_gen(12))