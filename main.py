Program_Loop = True 



#Acquire user info
print('Hello, this program is here to help manage your bank account info')

print('Please input your required info in the below sections.')

in_use = True
age = input('What is your age?')
name = input('Alright, what is your name?')

user_confirmation = input(f'So your name is {name}, and your age is {age}. If correct type YES, if not type NO')

if user_confirmation == 'YES' or user_confirmation == 'yes' or user_confirmation == 'Yes':
      print('Okay, let us move on.')

elif user_confirmation == 'NO' or user_confirmation == 'no' or user_confirmation == 'No':
     print('Alright, please re-enter the correct information.')
  return in_use
  
#Have them make a pin


