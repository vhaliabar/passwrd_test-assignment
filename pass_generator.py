#!/usr/bin/env python3

import string
import random

## characters to generate password from
characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_random_password():
	## shuffling the characters
	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(14):
		password.append(random.choice(characters))
    
	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	print("".join(password))



## invoking the function      
if __name__ == '__main__':
    generate_random_password()
    
    
## new line