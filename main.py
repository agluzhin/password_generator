# Import "random" and "string" module
import random
import string

# Creating variable in which user can pass the password's length.
password_length = int(input())

# Creating a storage of all possible elements.
elements = string.digits + string.ascii_letters + string.punctuation

# Creating a cycle in which new password get random element from element's storage.
new_password = ''.join(
    random.choice(elements)
    for _ in range(password_length)
)

print(new_password)
