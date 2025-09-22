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

    def get_customers(self):
        try:
            with open(self.file, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.customers.append(row)
                return self.customers
            # for info in self.customers:
            #     return info
        except FileNotFoundError:
            print('file not found:(')


#Source: https://www.youtube.com/watch?v=Kk2TkaQ2Y3Q&t=28s
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
    
    def save_update(self,list):
        with open(self.file, 'w',newline="" ) as file:
            fieldnames =['account_id', 'first_name', 'last_name', 'password', 'balance_checking', 'balance_savings']
            writer = csv.DictWriter(file, fieldnames= fieldnames)
            writer.writeheader()
            writer.writerows({
                'account_id':info['account_id'], 
                'first_name': info['first_name'] ,
                'last_name': info['last_name'],
                'password': info['password'],
                'balance_checking': info['balance_checking'],
                'balance_savings': info['balance_savings']
            } 
                for info in list)

    def add_customer(self,customer):
        self.customers.append(customer)
        self.save() 

    def customer_info(self, str):
        for i in self.customers:
            if str in i.first_name:
                i.info()

    def update_customer(self, data):
            # try:
                users= []
                try:
                    with open(self.file, "r") as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            users.append(row)
                    # for info in self.customers:
                    #     return info
                except FileNotFoundError:
                    print('file not found:(')
                # print(users)
                for line in users:
                    if line['first_name'] == data['first_name']:
                        # print(line)
                        line.update(self.customers)
                        # print(line)
                # print(users)
                self.save_update(users)




class Account (Bank):
    def __init__(self, file ):
        super().__init__(file)
        self.islogin = False
        
    

    def login(self,first_name, last_name, password ):
        print('hello from here')
        try:
            self.customers= self.get_customers()
            for info in self.customers:
                # firsts.append(info['first_name'])
                # print(info['first_name'])
                if first_name in info['first_name']:
                    if last_name in info['last_name']:
                        if password in info['password']:
                            self.islogin = True
                            self.customers =info
                            # print(self.customers)
                            print('you have been loged in ')
                #         else:
                #             print('pass no')
                #             # raise ValueError
                #     else:
                #         print('entered flast no')
                #         # raise ValueError
                # else:
                #     print('entered first no')

                    # raise ValueError
        except ValueError:
            #how to rase diffrent message for diffrent error???
            print('entered nonono')


#ADD THE Overdraft Protection 
    def withdraw_from_savings(self, price):
            # HANNDEL THIS ERROR*********************
            price = int(price)
            if self.islogin == False:
                # raise loginError
                print('please login first')
            else:
                # for info in self.customers:
                current_balance_checking =float(self.customers.get("balance_checking"))
                if price>= current_balance_checking:
                    #add fee
                    pass
                    # print('You have overdraft so a overdraft protection fee of 35 SAR will be apply')
                elif price > 0:
                    current_balance_checking -= price
                    self.customers.get("balance_checking")
                    for info in self.customers:
                        if info == 'balance_checking':
                            self.customers.update({info:current_balance_checking })
                    # print(self.customers)
                    # self.customers
                    self.update_customer( self.customers)
                else:
                    print('number must be >0')




    #ADD THE Overdraft Protection 
    def withdraw_from_checking(self, price):
            # HANNDEL THIS ERROR*********************
            price = int(price)
            if self.islogin == False:
                # raise loginError
                print('please login first')
            else:
                # for info in self.customers:
                current_balance_savings =float(self.customers.get("balance_savings"))
                if price>= current_balance_savings:
                    #add error handrling
                    pass
                    # print('You have overdraft so a overdraft protection fee of 35 SAR will be apply')
                elif price > 0:
                    current_balance_savings -= price
                    self.customers.get("balance_savings")
                    for info in self.customers:
                        if info == 'balance_savings':
                            self.customers.update({info:current_balance_savings })
                    # print(self.customers)
                    # self.customers
                    self.update_customer( self.customers)
                else:
                    print('number must be >0')
                



    def deposit_into_savings(self, amount):
        amount = int(amount)
        if amount < 1:
            pass
            # raise error
        else:
            new_balance_savings =int(self.customers.get("balance_savings"))
            new_balance_savings += amount
            self.customers.get("balance_savings")
            for info in self.customers:
                if info == 'balance_savings':
                    self.customers.update({info:new_balance_savings })
            # print(self.customers)
            # self.customers
            self.update_customer( self.customers)


    def deposit_into_checking(self, amount):
        amount = int(amount)
        if amount < 1:
            pass
            # raise error
        else:
            new_balance_checking =int(self.customers.get("balance_checking"))
            new_balance_checking += amount
            self.customers.get("balance_checking")
            for info in self.customers:
                if info == 'balance_checking':
                    self.customers.update({info:new_balance_checking })
            # print(self.customers)
            # self.customers
            self.update_customer( self.customers)

        
    def transfer_from_savings_to_checking(self, amount):
        amount = int(amount)
        if amount < 1:
            pass
            # raise error
        else:
            current_balance_savings =float(self.customers.get("balance_savings"))
            if amount>= current_balance_savings:
                #add error handrling
                pass
                # print('You have overdraft so a overdraft protection fee of 35 SAR will be apply')
            elif amount > 0:
                current_balance_savings -= amount
                new_balance_checking =float(self.customers.get("balance_checking"))
                new_balance_checking += amount
                # self.customers.get("balance_savings")
                for info in self.customers:
                    if info == 'balance_savings':
                        self.customers.update({info:current_balance_savings })
                    if info == 'balance_checking':
                        self.customers.update({info:new_balance_checking })
                    
                # print(self.customers)
                # self.customers
                self.update_customer( self.customers)
            else:
                print('number must be >0')





    def transfer_from_checking_to_savings(self, amount):
            amount = int(amount)
            if amount < 1:
                pass
                # raise error
            else:
                new_balance_checking =float(self.customers.get("balance_checking"))
                if amount>= new_balance_checking:
                    #add error handrling
                    pass
                    # print('You have overdraft so a overdraft protection fee of 35 SAR will be apply')
                elif amount > 0:
                    new_balance_checking -= amount
                    current_balance_savings =float(self.customers.get("balance_savings"))
                    current_balance_savings += amount
                    # self.customers.get("balance_savings")
                    for info in self.customers:
                        if info == 'balance_savings':
                            self.customers.update({info:current_balance_savings })
                        if info == 'balance_checking':
                            self.customers.update({info:new_balance_checking })
                        
                    # print(self.customers)
                    # self.customers
                    self.update_customer( self.customers)
                else:
                    print('number must be >0')


    






bank = Bank('bank.csv')
print('**** Welcome To This Bank ****')
# first_name=input('Enter Your First Name: ')
# last_name=input('Enter Your last Name: ')
# first_name=input('Enter Your First Name: ')
# first_name=input('Enter Your First Name: ')
# first_name=input('Enter Your First Name: ')

# bank.add_customer(Customer('Rama', 'Khalid', 'Rama123', 20000, 5000))
# bank.add_customer(Customer('sara', 'aaaa', '1221', 20000, 5000))
# ctr=Customer('Rama', 'Khalid', 'Rama123', 20000, 5000)

new_account =Account('bank.csv')
new_account.login('Rama', 'Khalid', 'Rama123')
# new_account.deposit_into_checking(500)
# new_account.deposit_into_savings(500)
# new_account.withdraw_from_checking(80)
# new_account.withdraw_from_savings(80)
# new_account.transfer_from_savings_to_checking(20)
new_account.transfer_from_checking_to_savings(20)
# bank.update_customer()
# print(new_account.customers)

# print(bank.get_customers())
# bank.customer_info('Rama')
