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

    
class Bank:
    def __init__(self, file):
        self.file = file
        self.customers = []

    def git_customers(self):
        try:
            with open(self.file, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.customers.append(row)

            for info in self.customers:
                print(info)
        except FileNotFoundError:
            print('file not found:(')

    def save(self):
        with open(self.file, 'a',newline="" ) as file:
            fieldnames =['account_id', 'first_name', 'last_name', 'password', 'balance_checking', 'balance_savings']
            writer = csv.DictWriter(file, fieldnames= fieldnames)
            writer.writerows({
                'account_id':info.account_id, 
                'first_name': info.first_name ,
                'last_name': info.last_name,
                'password': info.password,
                'balance_checking': info.balance_checking,
                'balance_savings': info.balance_savings

            } 
                for info in self.customers)

    def add_customer(self,customer):
        self.customers.append(customer)
        self.save()     
