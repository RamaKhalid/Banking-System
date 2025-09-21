import csv


class Customer:
    account_id =10006
    def __init__(self,first_name, last_name, password, balance_checking, balance_savings):
        self.account_id = Customer.account_id
        self.first_name =first_name
        self.last_name =last_name
        self.password =password
        self.balance_checking =balance_checking
        self.balance_savings =balance_savings
        Customer.account_id += 1

    def info(self):
        #chang it to retern for the testt
        print(f'First Name: {self.first_name} \nLast Name: {self.last_name} \nPassword: {self.password} \nBalance Checking: {self.balance_checking} \nBalance_Savings: {self.balance_savings}')

    
