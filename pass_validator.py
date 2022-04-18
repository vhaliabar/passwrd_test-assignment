#!/usr/bin/env python3

import string
import sys
test_passwrd = sys.argv[1]

def password_check(passwd):
    val = True
    
    if not any(char.isupper() for char in passwd) or not any(char.islower() for char in passwd):
        print('- Password must contain both lowercase and uppercase letters')
        val = False     
             
    if not any(char.isdigit() for char in passwd):
        print('- Password must contain digits')
        val = False
          
    if not any(char in string.punctuation for char in passwd):
        print('- Password must contain at least one punctuation character(!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~)')
        val = False
    
    if len(passwd) <= 14:
        print('- Password should be at least 14 characters long')
        val = False
    
    if val:
        return f'Strong password'
  
# Driver Code        
if __name__ == '__main__':
    password_check(test_passwrd)