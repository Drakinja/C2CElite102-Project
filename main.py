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
   pin = input('Please create a pin for your account contain only numbers. Do not share or spread this for safety of your account')

elif account_creation == 'No':
     print('Alright, please enter your pin to access your account information.')

def display_menu():
    print("\n Here is what you can do In your account")
    print("1. Create savings")
    print("2. Check balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. close Program\n")

def user_selection():
      in_use = True
      user_choice = input("Enter a number through 1-4: ")

      if user_choice.isdigit():  # Check if the input consists of digits
        user_choice = int(user_choice)
        if 1 <= user_choice <= 5:
            if user_choice == 1:
              def savings_menu():
                 print("\n **what type of savings would you like to make?**")
                 print("1. Student Account")
                 print("2. Retirement Account")
                 print("3. Savings Account")
                 print("4.  Return to Menu\n") 
               
            elif user_choice == 2:
                 print(f'You have dollars in your account')
            elif user_choice == 3:
                 print('How much you youl like to deposit?')   
            elif user_choice == 4:
                 print('How much would you like')
            elif user_choice == 5:    
                 return in_use       

connection.close()