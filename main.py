# Import "random" module
import random

# Creating variable in which user can pass the password's length.
password_length = int(input())

# Creating a storage for the all elements in future password.
new_password = []

# Creating a storage of all possible elements.
elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
    "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Creating a cycle in which new password get random element from element's storage.	
for i in range(0, password_length):
	random_element = random.choice(elements)
	new_password.append(random_element)
	i += 1

# Creating variable in which list is converted to a string for further output.
result = ''.join(map(str, new_password))
print(result)
	


