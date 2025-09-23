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
        return(f'First Name: {self.first_name} \nLast Name: {self.last_name} \nPassword: {self.password} \nBalance Checking: {self.balance_checking} \nBalance_Savings: {self.balance_savings}')

    
class Bank:
    def __init__(self, file):
        self.file = file
        self.customers = []
        self.allUsers= []

    def get_customers(self):
        try:
            with open(self.file, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.allUsers.append(row)
                return self.allUsers
        except FileNotFoundError:
            print(f'Sorry {file} file not found:(')


#Source: https://www.youtube.com/watch?v=Kk2TkaQ2Y3Q&t=28s
    def save(self):
        try:
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
        except FileNotFoundError:
            print(f'Sorry {file} file not found:(')
        # except TypeError:
        #     pass
        # except IndentationError:
        #     pass

    
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
        firsts=[]
        lasts=[]
        passwords=[]
        print('hello from here')
        try:
            self.customers= self.get_customers()
            #ASK CONOR ABOUT THIS!!!!!!!!!!!!!!!!!!!!!!!
            for info in self.customers:
                firsts.append(info['first_name'])
                lasts.append(info['last_name'])
                passwords.append(info['password'])
                if first_name in info['first_name']:
                    if last_name in info['last_name']:
                        if password in info['password']:
                            self.customers =info

            if first_name in firsts:
                if last_name in lasts:
                    if password in passwords:
                        self.islogin = True
                        # self.customers =info
                        # print(self.customers)
                        print(f'Welcome {first_name}👋, you have been loged in successfully🎉 ')
                    else:
                        print('pass no')
                        # raise ValueError
                        return
                else:
                    print('entered last no')
                    # raise ValueError
                    return
            else:
                print('entered first no')
                return
                # raise ValueError
        except ValueError:
            #how to rase diffrent message for diffrent error???
            print('entered nonono')

    def overdraft_Protection(self, balance, amount):
        # if balance<0:


        new_balance =float(balance)
        new_balance -= amount
        if new_balance < -100:
            print('Sorry You can\'t Do This Transaction as you Exceeds the minimum limit allowed (less than -100$)' )
            return balance
        elif balance>0 and new_balance<0:
            print(f'Your account have only {balance}$ and overdraft will charge you with 35$ are sure to continue?')
            # Find better message
            charge = input('To continue Enter Y or N to stop')
            charge = charge.upper()
            if charge == 'Y':
                print('A 35$ have been deduct from you account, Please Pay Your Fee As Soon As possible ')
                new_balance -= 35
                return new_balance
            if charge == 'N':
                print('Your Transaction is stoped')
                return balance
        elif balance <0 and new_balance>= -100:
            return new_balance


        


#ADD THE Overdraft Protection 
    def withdraw_from_checking(self, price):
            # HANNDEL THIS ERROR*********************
            price = int(price)
            if self.islogin == False:
                # raise loginError
                print('please login first')
            else:
                current_balance_checking =float(self.customers.get("balance_checking"))
                if price > current_balance_checking:
                    new_balance_checking = self.overdraft_Protection(current_balance_checking , price)
                    if new_balance_checking < current_balance_checking:
                        for info in self.customers:
                            if info == 'balance_checking':
                                self.customers.update({info:new_balance_checking })
                        self.update_customer( self.customers)
                    else:

                        pass
                    # print('You have overdraft so a overdraft protection fee of 35 SAR will be apply')
                elif price > 0 and price <= current_balance_checking :
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
    def withdraw_from_savings(self, price):
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


    def transfer_checking_to_another_account(self, amount, user_account_id):
        users=[]
        user={}
        amount = int(amount)
        if amount < 1:
            pass
            # raise error
        else:
            users= self.get_customers()
            for line in users:
                if user_account_id in line['account_id']:
                    user.update(line)
                    break
            # print(user)
            customer_balance_checking =float(self.customers.get("balance_checking"))
            if amount>= customer_balance_checking:
                #add error handrling
                pass
                # print('You have overdraft so a overdraft protection fee of 35 SAR will be apply')
            else:
                customer_balance_checking -= amount
                user_checking =float(user.get("balance_checking"))
                user_checking += amount
                for info in self.customers:
                    if info == 'balance_checking':
                        self.customers.update({info:customer_balance_checking })
                        break
                self.update_customer( self.customers)
                for info in user:
                    # print(info) 
                    if info == 'balance_checking':
                        user.update({info:user_checking })
                        # print(user)
                        break
                self.update_customer(user)


    def transfer_savings_to_another_account(self, amount, user_account_id):
        users=[]
        user={}
        amount = int(amount)
        if amount < 1:
            pass
            # raise error
        else:
            users= self.get_customers()
            for line in users:
                if user_account_id in line['account_id']:
                    user.update(line)
                    break
            # print(user)
            customer_balance_savings =float(self.customers.get("balance_savings"))
            if amount>= customer_balance_savings:
                #add error handrling
                pass
                # print('You have overdraft so a overdraft protection fee of 35 SAR will be apply')
            else:
                customer_balance_savings-= amount
                user_checking =float(user.get("balance_checking"))
                user_checking += amount
                for info in self.customers:
                    if info == 'balance_savings':
                        self.customers.update({info:customer_balance_savings })
                        break
                self.update_customer( self.customers)
                for info in user:
                    # print(info) 
                    if info == 'balance_checking':
                        user.update({info:user_checking })
                        # print(user)
                        break
                self.update_customer(user)





bank = Bank('bank.csv')
# 

# bank.add_customer(Customer('sara', 'aaaa',"jjj" , 20000, 5000))
# ctr=Customer('Rama', 'Khalid', 'Rama123', 20000, 5000)

new_account =Account('bank.csv')
new_account.login('Rama', 'Khalid', 'Rama123')
# # new_account.deposit_into_checking(500)
# # new_account.deposit_into_savings(500)
new_account.withdraw_from_checking(80)
# # new_account.withdraw_from_savings(80)
# # new_account.transfer_from_savings_to_checking(20)
# # new_account.transfer_from_checking_to_savings(20)
# new_account.transfer_checking_to_another_account(360, '10003' )
# bank.update_customer()
# print(new_account.customers)

# print(bank.get_customers())
# bank.customer_info('Rama')
