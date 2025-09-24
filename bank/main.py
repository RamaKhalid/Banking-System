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
                option= input("\nPlease Enter The Service Number: ")
                option= int(option)
                if option == 1:
                    while True:
                        print('\nChoice Your Account ')
                        print('1. withdraw Money from checking')
                        print('2. withdraw Money from savings')
                        print('5. Go BAck to the Services page')
                        option= input("\nPlease Enter The Service Number: ")
                        option= int(option)
                        if option == 1:
                            print('\nwithdraw Money from checking')
                            amount = input('Pleas Enter the Amount You Like To Withdraw: ')
                            amount =int(amount)
                            new_account.withdraw_from_checking(amount)
                        if option == 2:
                            pass
                if option == 2:
                    pass

                if option == 3:
                    pass

                if option == 4:
                    pass

                if option == 5:
                    pass





            #         if choice == 1:
            # new_account =Account('bank.csv')
            # while True:
            #     try:
            #         first_name=input('Enter Your First Name: ')
            #         if first_name ==' ' or (not first_name.isalpha()):
            #             raise MissingValue('\nPlease Enter a Real Name\n')
            #         else:
            #             break
            #     except MissingValue as e:
            #         print(e)
            # while True:
            #     try:
            #         last_name=input('Enter Your last Name: ')
            #         if last_name == ' ' or (not last_name.isalpha()):
            #             raise MissingValue('\nPlease Enter a Real Name\n')
            #         else:
            #             break
            #     except MissingValue as e:
            #         print(e)
            # while True:
            #     try:
            #         password=input('Enter Your password: ')
            #         if password == "" :
            #             raise MissingValue('\nPlease Enter A Proper Password\n')
            #         else:
            #             break
            #     except MissingValue as e:
            #         print(e)
            # new_account.login(first_name, last_name, password)
            # if new_account.islogin == True:
            #     while True:
            #         print(f'\n**** Welcome {first_name}👋 ****')
            #         print('What would you like to do?')
            #         print('1. withdraw Money')
            #         print('2. Deposit Money')
            #         print('3. Transfer Money')
            #         print('4. See My Account information')
            #         print('5. Go BAck to the main page')
            #         option= input("\nPlease Enter The Service Number: ")
            #         option= int(option)

            #         if option == 1:
            #             while True:
            #                 print('\nChoice Your Account ')
            #                 print('1. withdraw Money from checking')
            #                 print('2. withdraw Money from savings')
            #                 print('5. Go BAck to the Services page')
            #                 option= input("\nPlease Enter The Service Number: ")
            #                 option= int(option)
            #                 if option == 1:
            #                     print('\nwithdraw Money from checking')
            #                     amount = input('Pleas Enter the Amount You Like To Withdraw: ')
            #                     amount =int(amount)

            #                     new_account.withdraw_from_checking(amount)

            #                 if option == 2:
            #                     pass


            
















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

        if choice !=1 or choice !=2:
            raise ValueError
    except ValueError:
        print("Please Enter a vaild input")
    except MissingValue as e:
        print(e)
    else:
        print(f'{first_name}\'s Account Have Been added successfully 🎉 \n')
        




