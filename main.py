import numbers
import random

lowercase = 'abcdefghijklmnopqrstuvwxyz' 
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
digits = '0123456789' 

add_lowercase = input('Add lowercase letters? (yes/no): ')
add_uppercase =  input ('Add uppercase letters? (yes/no):  ') 
add_numbers =  input ('Add numbers: ') 

# كتابة دالة لتوليد كلمة مرور عشوائية
def generate_password():
    length = int(input("Enter the length of the password: ")) 
    characters = ''
    
    if add_lowercase.lower() == 'yes':
            characters += lowercase
    if add_uppercase.lower() == 'yes':
            characters += uppercase
    if add_numbers.lower() == 'yes':
            characters += digits
    if not characters:
        print("No character types selected. Please select at least one type.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Generated Password:", generate_password())