from bank.bank import *
from exceptions import*

bank = Bank('bank.csv')
while True:
    print('\n**** Welcome To This Bank ****')
    print('What would you want to do?')
    print('1. Login')
    print('2. Add New Customer')
    try:
        choice= input("Please Enter The Service Number: ")
        choice =int(choice)
        if choice < 1 or choice >2:
            raise ValueError
    except ValueError :
        print("Please Enter a vaild input 1 or 2")
    

    if choice == 1:
        while True:
            new_account =Account('bank.csv')
            while True:
                try:
                    user_id=input('Please Enter Your ID: ')
                    if user_id ==' ' or (not user_id.isdigit()):
                        raise MissingValue('\nPlease Enter Your Valid ID\n')
                    else:
                        break
                except MissingValue as e:
                    print(e)
            while True:
                try:
                    password=input('Enter Your password: ')
                    if password == "" :
                        raise MissingValue('\nPlease Enter A Proper Password\n')
                    else:
                        break
                except MissingValue as e:
                    print(e)
            
            new_account.login(user_id, password) 
    
            if new_account.islogin == True:
                break
        user =new_account.customers
        while True:
            print(f'\n**** Welcome {user['first_name']}👋 ****')
            print('What would you like to do?')
            print('1. withdraw Money')
            print('2. Deposit Money')
            print('3. Transfer Money')
            print('4. See My Account information')
            print('5. Go BAck to the main page')
            try:
                option= input("\nPlease Enter The Service Number: ")
                option= int(option)
                if option <1 or option >5:
                    raise ValueError
            except ValueError :
                print("Please Enter a vaild input from 1 to 5")

            if option == 1:
                while True:
                    print('\nChoice Your Account ')
                    print('1. withdraw Money from checking')
                    print('2. withdraw Money from savings')
                    print('3. Go BAck to the Services page')
                    try:
                        withdraw_option= input("\nPlease Enter The Service Number: ")
                        withdraw_option= int(withdraw_option)
                        if withdraw_option <1 or withdraw_option >3:
                            raise ValueError
                    except ValueError :
                        print("Please Enter a vaild input from 1 to 3")
                    if withdraw_option == 1:
                        while True:    
                            try:
                                print('\n**** withdraw Money from checking ****')
                                amount = input('Pleas Enter the Amount You Like To Withdraw: ')
                                amount =int(amount)
                                new_account.withdraw_from_checking(amount)
                            except ValueError :
                                print("Please Enter a vaild amount of money")
                            else:
                                break
                    if withdraw_option == 2:
                        while True:    
                            try:
                                print('\n**** withdraw Money from Savings ****')
                                amount = input('Pleas Enter the Amount You Like To Withdraw: ')
                                amount =int(amount)
                                new_account.withdraw_from_savings(amount)
                            except ValueError :
                                print("Please Enter a vaild amount of money")
                            else:
                                break
                    if withdraw_option == 3:
                        break

            if option == 2:
                while True:
                    print('\nChoice Your Account ')
                    print('1. Deposit Money To checking')
                    print('2. Deposit Money To savings')
                    print('3. Go BAck to the Services page')
                    try:
                        Deposit_option= input("\nPlease Enter The Service Number: ")
                        Deposit_option= int(Deposit_option)
                        if Deposit_option <1 or Deposit_option >3:
                            raise ValueError
                    except ValueError :
                        print("Please Enter a vaild input from 1 to 3")
                    
                    if Deposit_option == 1:
                        while True:    
                            try:
                                print('\n**** Deposit Money To checking ****')
                                amount = input('Pleas Enter the Amount You Like To Deposit: ')
                                amount =int(amount)
                                new_account.deposit_into_checking(amount)
                            except ValueError :
                                print("Please Enter a vaild amount of money")
                            else:
                                break

                    if Deposit_option == 2:
                        while True:    
                            try:
                                print('\n**** Deposit Money To Savings ****')
                                amount = input('Pleas Enter the Amount You Like To Deposit: ')
                                amount =int(amount)
                                new_account.deposit_into_savings(amount)
                            except ValueError :
                                print("Please Enter a vaild amount of money")
                            else:
                                break

                    if Deposit_option == 3:
                        break

            if option == 3:
                pass
                
            if option == 4:
                print(bank.customer_info())
            if option == 5:
                break















        if choice == 2:
                try:
                    while True:
                        try:
                            first_name=input('Enter Your First Name: ')
                            if first_name ==' ' or (not first_name.isalpha()):
                                raise MissingValue('\nPlease Enter a Real Name\n')
                            else:
                                break
                        except MissingValue as e:
                            print(e)

                    while True:
                        try:
                            last_name=input('Enter Your last Name: ')
                            if last_name == ' ' or (not last_name.isalpha()):
                                raise MissingValue('\nPlease Enter a Real Name\n')
                            else:
                                break
                        except MissingValue as e:
                            print(e)
                    while True:
                        try:
                            password=input('Enter Your password: ')
                            if password == "" :
                                raise MissingValue('\nPlease Enter A Proper Password\n')
                            else:
                                break
                        except MissingValue as e:
                            print(e)
                    while True:
                        try:
                            balance_checking=input('Enter Your balance checking: ')
                            if balance_checking == "" or (not balance_checking.isdigit()) :
                                raise MissingValue('\nPlease enter a proper checking\n')
                            else:
                                break
                        except MissingValue as e:
                            print(e)
                    while True:
                        try:
                            balance_savings=input('Enter Your balance savings: ')
                            if balance_savings == "":
                                balance_savings = 0.0
                                break
                            elif not balance_savings.isdigit():
                                raise MissingValue('\nPlease enter a proper Savings that contain only numbers\n')                           
                            else:
                                break
                        except MissingValue as e:
                            print(e)
                    bank.add_customer(Customer(first_name, last_name, password, balance_checking, balance_savings))
                    print('')
                    print(bank.customer_info())

                except MissingValue as e:
                    print(e)

        
    # except ValueError:
    #     print("Please Enter a vaild input")
    # except MissingValue as e:
    #     print(e)
    # else:
    #     print(f'{first_name}\'s Account Have Been added successfully 🎉 \n')
        




