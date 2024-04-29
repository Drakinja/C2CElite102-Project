program_loop = True

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

   cursor = connection.cursor()

   addData = ("INSERT INTO pin_management (Usernames, Pins) VALUES ({name},{pin})")

   cursor.execute(addData)

   connection.commit()

   cursor.close()

elif account_creation == 'No':
     print('Alright, please enter your pin to access your account information.')
     cursor = connection.cursor()

     testQuery = ("SELECT * FROM pin_management")

     cursor.execute(testQuery)

     for item in cursor:
       print(item)

     cursor.close()

else:
     print('This is not a correct response, please try again.')

def display_menu():
    print("\n Here is what you can do In your account")
    print("1. Create savings")
    print("2. Check balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. End Program & log out\n")

    def user_selection():
        in_use = True
        user_choice = input("Enter a number through 1-4: ")

        if user_choice.isdigit():  # Check if the input consists of digits
          user_choice = int(user_choice)
          if 1 <= user_choice <= 5: #Create functions below for each option of menu
              if user_choice == 1:
               def savings_menu():  #make a menu for savings
                   print("\n **what type of account would you like to make?**")
                   print("1. Student Account")
                   print("2. Retirement Account")
                   print("3. Savings Account")
                   print("4.  Return to Menu\n")                    
                   def savings_choice(): #function to go into savings choice options and management
                       if savings_choice.isdigit():    
                         savings_choice = int(savings_choice)
                         if 1 <= savings_choice <= 4:
                                if savings_choice == 1:
                                   student_deposit = input('How much do you want to deposit in your Student account?')                             
                                   cursor = connection.cursor()

                                   addData = ("INSERT INTO pin_management (Student balance) VALUES ({student_deposit})")

                                   cursor.execute(addData)

                                   connection.commit()

                                   cursor.close()

                                elif savings_choice == 2:
                                   retirement_deposit = input('How much do you want to deposit in your Retirement Account?')
                                   cursor = connection.cursor()

                                   addData = ("INSERT INTO pin_management (Retirement Balance) VALUES ({retirement_deposit})")

                                   cursor.execute(addData)

                                   connection.commit()

                                   cursor.close()

                                elif savings_choice == 3:
                                    savings_deposit = input('How much do you want to deposit in your Savings Account?')
                                    cursor = connection.cursor()

                                    addData = ("INSERT INTO pin_management (Savings) VALUES ({savings_deposit})")

                                    cursor.execute(addData)

                                    connection.commit()

                                    cursor.close()
                                elif savings_choice == 4:
                                    return in_use              
              elif user_choice == 2: #Tell them balance
                   print(f'You have a balance of dollars in your account')           
              elif user_choice == 3: #Input added ammount & tell them new balance
                  normal_deposit = input('How much you youl like to deposit?') 
                  cursor = connection.cursor()

                  addData = ("INSERT INTO pin_management (Normal balance) VALUES ({normal_deposit})")

                  cursor.execute(addData)

                  connection.commit()

                  cursor.close()
                
              elif user_choice == 4: #Input removed ammount & tell them new balance
                  normal_withdraw = input('How much would you like to withdraw?')
              elif user_choice == 5:
                   in_use = False      
              else: #create a function in case they make an invalid choice.
                  print('This is not an available option.')
                  return in_use 
while program_loop:
  display_menu()
  in_use = user_selection()
  program_loop = in_use 


connection.close()