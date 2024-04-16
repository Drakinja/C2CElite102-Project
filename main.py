import mysql.connector
connection = mysql.connector.connect(user = 'william', database = 'Local instance MySQL80', password = 'Dynamowill102008')


#Welcome user to bot
print('Welcome to ... Bank account manager bot.')

#confirm if new user or not
account_creation = input('User, would you like to create a new account, type Yes. If you already have one, type No. Be mindful it is caps sensitive.')

if account_creation == 'Yes':
#Acquire user info
   print('Please input your required info for account creation in the below sections.')

   age = input('What is your age?')
   name = input('Alright, what is your name?')

   print('So your name is {name} and your age is {age}. If this information is incorrect please restart the program.')

   #Have them make a pin
   pin = input('Please create a pin for your account. Do not share or spread this for safety of your account')

elif account_creation == 'No':
     print('Alright, please enter your pin to access your account information.')
  


connection.close()