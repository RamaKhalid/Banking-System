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
            pass
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
                            elif not balance_savings.isdigit():
                                raise MissingValue('\nPlease enter a proper Savings that contain only numbers\n')                           
                            else:
                                break
                        except MissingValue as e:
                            print(e)
                    bank.add_customer(Customer(first_name, last_name, password, balance_checking, balance_savings))
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




