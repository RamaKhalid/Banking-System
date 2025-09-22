from bank.bank import *

bank = Bank('bank.csv')
while True:
    print('**** Welcome To This Bank ****')
    print('What would you want to do?')
    print('1. Login')
    print('2. Add New Customer')
    choice= input("Please Enter The Service Number: ")

    if choice == 1:
        pass

    if choice == 2:
        try:
            first_name=input('Enter Your First Name: ')
            last_name=input('Enter Your last Name: ')
            password=input('Enter Your password: ')
            balance_checking=input('Enter Your balance checking: ')
            balance_savings=input('Enter Your balance savings: ')

            bank.add_customer(Customer(first_name, last_name, password, balance_checking, balance_savings))
        except ValueError:
            print("Please Enter a vaild input")
        else:
            print(f'{first_name}\'s Account Have Been added successfully 🎉')




