from bank.bank import *
from bank.exceptions import*
import re

bank = Bank('bank.csv')
while True:
    print('\n**** Welcome To This Bank ****')
    print('What would you want to do?')
    print('1. Login')
    print('2. Add New Customer')
    print('3. Reward The Top Customer💰')
    try:
        choice= input("Please Enter The Service Number: ")
        choice =int(choice)
        if choice < 1 or choice >3:
            raise ValueError
    except ValueError :
        print("Please Enter a vaild input 1 or 3")
    

    if choice == 1:
        while True:
            new_account =Account('bank.csv')
            while True:
                try:
                    user_id=input('Please Enter Your ID: ')
                    if user_id ==' ' or (not user_id.isdigit()):
                        raise MissingValue('\nPlease Enter a Valid ID\n')
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
                
                    
            try:
                print(new_account.login(user_id, password)) 
            except UseeIsNOTlogin as e:
                    print(e)

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
            print('5. Display Transaction History')
            print('6. Go BAck to the main page')
            try:
                option= input("\nPlease Enter The Service Number: ")
                option= int(option)
                if option <1 or option >6:
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
                            except Declined:
                                pass
                            except UseeIsNOTlogin:
                                print('Sorry You Neet To Login First')
                                break
                            except Deactivate:
                                print(f'Dear {user['first_name']} Your Accout Is Deactivate, \nKindly settle your outstanding balance. The amount credited to your account is {user['balance_checking']}$')
                                break
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
                            except Declined:
                                pass
                            except UseeIsNOTlogin:
                                print('Sorry You Neet To Login First')
                                break
                            except Deactivate:
                                print(f'Dear {user['first_name']} Your Accout Is Deactivate, \nKindly settle your outstanding balance. The amount credited to your account is {user['balance_checking']}$')
                                break
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
                            except UseeIsNOTlogin:
                                print('Sorry You Neet To Login First')
                                break
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
                            except UseeIsNOTlogin:
                                print('Sorry You Neet To Login First')
                                break
                            else:
                                break

                    if Deposit_option == 3:
                        break

            if option == 3:
                while True:
                    print('\nChoice Your Account ')
                    print('1. Transfer Mony From Savings To Checking')
                    print('2. Transfer Money From Checking To Savings')
                    print('3. Transfer Money From Checking To Another Account')
                    print('4. Transfer Money From Saving To Another Account')
                    print('5. Go BAck to the Services page')
                    try:
                        Transfer_option= input("\nPlease Enter The Service Number: ")
                        Transfer_option= int(Transfer_option)
                        if Transfer_option <1 or Transfer_option >5:
                            raise ValueError
                    except ValueError :
                        print("Please Enter a vaild input from 1 to 5")
                    if Transfer_option == 1:
                        while True:    
                            try:
                                print('\n**** Transfer Mony From Savings To Checking ****')
                                amount = input('Pleas Enter the Amount You Like To Transfer: ')
                                amount =int(amount)
                                new_account.transfer_from_savings_to_checking(amount)
                            except ValueError :
                                print("Please Enter a vaild amount of money")
                            except Declined:
                                pass
                            except UseeIsNOTlogin:
                                print('Sorry You Need To Login First')
                                break
                            else:
                                break
                        
                    if Transfer_option == 2:
                        while True:    
                            try:
                                print('\n**** Transfer Money From Checking To Savings ****')
                                amount = input('Pleas Enter the Amount You Like To Transfer: ')
                                amount =int(amount)
                                new_account.transfer_from_checking_to_savings(amount)
                            except ValueError :
                                print("Please Enter a vaild amount of money")
                            except Declined:
                                pass
                            except UseeIsNOTlogin:
                                print('Sorry You Neet To Login First')
                                break
                            except Deactivate:
                                print(f'Dear {user['first_name']} Your Accout Is Deactivate, \nKindly settle your outstanding balance. The amount credited to your account is {user['balance_checking']}$')
                                break
                            else:
                                break

                    if Transfer_option == 3:
                        while True:    
                            try:
                                print('\n**** Transfer Money From Checking To Another Account ****')
                                amount = input('Pleas Enter the Amount You Like To Transfer: ')
                                amount =int(amount)
                                other_id =input('Please Enter The ID For The Account You Want Transfer To: ')
                                new_account.transfer_checking_to_another_account(amount, other_id)
                            except ValueError :
                                print("Please Enter a vaild amount of money")
                            except Declined:
                                pass
                            except UseeIsNOTlogin:
                                print('Sorry You Neet To Login First')
                                break
                            except Deactivate:
                                print(f'Dear {user['first_name']} Your Accout Is Deactivate, \nKindly settle your outstanding balance. The amount credited to your account is {user['balance_checking']}$')
                                break
                            else:
                                break
                    if Transfer_option == 4:
                        while True:    
                            try:
                                print('\n**** Transfer Money From Savings To Another Account ****')
                                amount = input('Pleas Enter the Amount You Like To Transfer: ')
                                amount =int(amount)
                                new_account.transfer_savings_to_another_account(amount)
                            except ValueError :
                                print("Please Enter a vaild amount of money")
                            except Declined:
                                pass
                            except UseeIsNOTlogin:
                                print('Sorry You Neet To Login First')
                                break
                            except IdNotFound as e:
                                print(e)
                            else:
                                break
                    if Transfer_option == 5:
                        break
                
            if option == 4:
                print(new_account.customer_info())
                while True: 
                    back = input('\nIf you want to go back enter Q: ')
                    try:
                        back =back.upper()
                        if back == 'Q':
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print('Please Enter Q to Quit')
                        
                        

            if option == 5:
                new_account.get_transaction_hisory()
                while True:
                    back = input('\nIf you want to go back enter Q: ')
                    try:
                        back =back.upper()
                        if back == 'Q':
                            break
                        else:
                            raise ValueError 
                    except ValueError:
                        print('Please Enter Q to Quit')
                        

            if option == 6:
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
                            leter =any(l.isalpha() for l in password)
                            num =any(l.isdigit() for l in password)
                            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
                            if regex.search(password) != None and leter and num and len(password)>=8 :
                                break
                            else:
                                raise WeekPassword('Your Password is week, it should contain at least 8 characters with letters, numbers, and special characters')
                            
                    except MissingValue as e:
                        print(e)
                    except WeekPassword as e:
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
                while True:
                    try:
                        print('would you like to customize your overdraft limit? or keep it as defult as -$100 limit')
                        overdraft =input('Please Enter Y to customize it or N to keep the defult: ')
                        overdraft = overdraft.upper()
                        if overdraft =='N':
                            print('Thank you For Choosing This Bank! Your overdraft limit will be -$100')
                            overdraft_limit = -100
                            break
                        elif overdraft =='Y':
                            overdraft_limit= input('Please Enter The Limit You Want: ')
                            overdraft_limit = int(overdraft_limit)
                            if overdraft_limit < 0:
                                print(f'Thank you For Choosing This Bank! Your overdraft limit will be {overdraft_limit}$')
                                break
                            else:
                                raise MissingValue('\nPlease enter a overdraft_limit that is a negative Number\n')                  

                        else:
                            raise MissingValue('\nPlease enter  Y to customize it or N to keep the defult:')
                        
                    except MissingValue as e:
                        print(e)
                bank.add_customer(Customer(first_name, last_name, password, balance_checking, balance_savings,overdraft_limit))
                print('')
                print(bank.get_new_customer_info())
                
            except MissingValue as e:
                print(e)
    if choice == 3:
        bank.top_customer()
        while True:
            try:
                back= input('Enter B to Get Back To The Main Page: ')
                back =back.upper()
                if back== 'B':
                    break
                else:
                    raise ValueError
            except ValueError:
                print ('Please Enter B To Get Back')
        
    # except ValueError:
    #     print("Please Enter a vaild input")
    # except MissingValue as e:
    #     print(e)
    # else:
    #     print(f'{first_name}\'s Account Have Been added successfully 🎉 \n')
        




