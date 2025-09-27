import csv
from bank.exceptions import*
import datetime
import uuid
import random

class Customer:

    ids =[]
    id= ''
    try:
        with open('bank.csv', "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                ids.append(row['account_id'])
                id = int(ids[-1])+1
            
    except FileNotFoundError:
        print(f'Sorry {file} file not found:(')

    
    account_id =id
    
    def __init__(self,first_name, last_name, password, balance_checking, balance_savings, overdraft_limit):
        self.account_id = Customer.id
        self.first_name =first_name
        self.last_name =last_name
        self.password =password
        self.balance_checking =balance_checking
        self.balance_savings =balance_savings
        Customer.account_id += 1
        self.overdrafts = 0
        self.activation= 'activate'
        self.overdraft_limit = overdraft_limit



class Bank():
    def __init__(self, file):
        self.file = file
        self.customers = []
        self.allUsers= []
        self.transaction={}
        self.all_transactions =[]

        

    def get_id(self):
        for i in self.customers:
            return i.account_id

    def get_customers(self):
        try:
            with open(self.file, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.allUsers.append(row)
                return self.allUsers
        except FileNotFoundError:
            print(f'Sorry {self.file} file not found:(')


#Source: https://www.youtube.com/watch?v=Kk2TkaQ2Y3Q&t=28s
    def save(self):
        try:
            with open(self.file, 'a',newline="" ) as file:
                fieldnames =['account_id', 'first_name', 'last_name', 'password', 'balance_checking', 'balance_savings', 'overdrafts','activation','overdraft_limit']
                writer = csv.DictWriter(file, fieldnames= fieldnames)
                writer.writerows({
                    'account_id':info.account_id, 
                    'first_name': info.first_name ,
                    'last_name': info.last_name,
                    'password': info.password,
                    'balance_checking': info.balance_checking,
                    'balance_savings': info.balance_savings,
                    'overdrafts':0,
                    'activation': 'activate',
                    'overdraft_limit':info.overdraft_limit
                } 
                    for info in self.customers)
            print('New Account has been added successfully🎉')
        except FileNotFoundError:
            print(f'Sorry {self.file} file not found:(')
        

    def add_customer(self,customer):
        self.customers.append(customer)
        self.save() 

    def save_update(self,list):
        try:
            with open(self.file, 'w',newline="" ) as file:
                fieldnames =['account_id', 'first_name', 'last_name', 'password', 'balance_checking', 'balance_savings','overdrafts','activation','overdraft_limit']
                writer = csv.DictWriter(file, fieldnames= fieldnames)
                writer.writeheader()
                writer.writerows({
                    'account_id':info['account_id'], 
                    'first_name': info['first_name'] ,
                    'last_name': info['last_name'],
                    'password': info['password'],
                    'balance_checking': info['balance_checking'],
                    'balance_savings': info['balance_savings'],
                    'overdrafts': info['overdrafts'],
                    'activation': info['activation'],
                    'overdraft_limit':info['overdraft_limit']
                } 
                    for info in list)
        except FileNotFoundError:
            print(f'Sorry {file} file not found:(')


    def update_customer(self, data):
                users= []
                try:
                    with open(self.file, "r") as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            users.append(row)
                except FileNotFoundError:
                    print('file not found:(')
                for line in users:
                    if line['account_id'] == data['account_id']:
                        line.update(data)
                self.save_update(users)


    def get_new_customer_info(self ):
        for i in self.customers:
        # return(self.customers['account_id'])
            return (f'New Account Information: \nAccount_id: {i.account_id} \nFirst Name: {i.first_name} \nLast Name: {i.last_name} \nPassword: {i.password} \nBalance Checking: {i.balance_checking} \nBalance_Savings: {i.balance_savings} \nOverdrafts: {i.overdrafts} \nActivation: {i.activation} \nOverdraft_limit: {i.overdraft_limit}')


    def customer_info(self):
        return (f'Account_id: {self.customers['account_id']} \nFirst Name: {self.customers['first_name']} \nLast Name: {self.customers['last_name']} \nPassword: {self.customers['password']} \nBalance Checking: {self.customers['balance_checking']} \nBalance_Savings: {self.customers['balance_savings']} \nOverdrafts: {self.customers['overdrafts']} \nActivation: {self.customers['activation']} \n overdraft_limit: {self.customers['overdraft_limit']}')


    def top_customer(self):
        count =[]
        winer ={}
        self.allUsers= self.get_customers()
        for row in self.allUsers:
            count.append({'account_id':row['account_id'],
                        'total_balnce': float(row['balance_checking']) + float(row['balance_savings']) })
        winers = sorted(count,reverse =True, key=lambda d: d['total_balnce'])[:3]
        # print(winers)
        winerId =random.choice(winers)
        # return winer

        for row in self.allUsers:
            if  winerId['account_id'] == row['account_id']:
                winer.update(row)
        
        new_checking = float(winer['balance_checking'])
        new_checking += 100
        winer.update({'balance_checking':new_checking})
        self.update_customer(winer)
        print(f'\ncongratulation to {winer['first_name']} 🎉, \nThey Are One Of Our Top Customers!💰 With an account balance of $ {winerId['total_balnce']} they\'ll receive a $100 Reward🤑🎉\n')





class Account (Bank):
    def __init__(self, file ):
        super().__init__(file)
        self.islogin = False
        
        
    

    def login(self,userID, password ):
        idFound= False
        self.allUsers= self.get_customers()
        for info in self.allUsers:
            if userID in info['account_id']:
                idFound =True
                if password in info['password']:
                    self.islogin = True
                    self.customers =info
                    return(f'Welcome {info['first_name']}👋, you have been loged in successfully🎉 ')
                # else:
                #     print('User Not found please check your Password')
        if idFound == False or self.islogin==False :
            raise UseeIsNOTlogin('User Not found please check your ID or password')


    def overdraft_Protection(self, balance, amount):
        new_balance =float(balance)
        new_balance -= amount
        if new_balance < float(self.customers.get('overdraft_limit')):
            print(f'Sorry You can\'t Do This Transaction as you Exceeds the minimum limit allowed (less than {self.customers.get('overdraft_limit')}$)' )
            return balance
        elif new_balance<0 and (new_balance-35 > float(self.customers.get('overdraft_limit'))):
            print(f'Your account have only {balance}$ and overdraft will charge you with 35$ are sure to continue?')
            # Find better message
            charge = input('To continue Enter Y or N to stop: ')
            charge = charge.upper()
            if charge == 'Y':
                print('A 35$ have been deduct from you account, Please Pay Your Fee As Soon As possible ')
                new_balance -= 35
                self.overdrafts_count()
                # print(f' this is overdrafts: {self.customers['overdrafts']}')
                return new_balance
            elif charge == 'N':
                print('Your Transaction is stoped')
                return balance
            else:
                raise ValueError('Please Enter Y or N')
        elif balance <0 and new_balance>= float(self.customers.get('overdraft_limit')):
            if (self.overdrafts_count()):
                print('Your Transaction is stoped')
                return balance
            else:
                return new_balance


    def overdrafts_count(self):
        overdrafts = self.customers['overdrafts']
        overdrafts = int(overdrafts)
        # Handiling deactivate
        if overdrafts== 2:
            print('you over overdrafts U_U Your account will be deactivate ^3^')
            deactivate = 'deactivate'
            for info in self.customers:
                if info == 'activation':
                    self.customers.update({info:deactivate})
                    self.update_customer(self.customers)
            raise Deactivate
        elif overdrafts== 1:
            print(f'Dear {self.customers['first_name']} This will be Your second overdrafts and Continuing with this Transaction will Deactivate Your Account')
            sure= input('Are You Sure You Want To Continue With This Transaction? Y to Continue N to Stop: ')
            sure =sure.upper()
            if sure == 'Y':
                overdrafts +=1
                for info in self.customers:
                    if info == 'overdrafts':
                        self.customers.update({info:overdrafts})
            elif sure == 'N':
                return True
            else:
                raise ValueError('Please Enter Y or N')
        else:
            overdrafts +=1
            for info in self.customers:
                if info == 'overdrafts':
                    self.customers.update({info:overdrafts})


    def reactivate(self, user):
        # Handeling reactivate account
        activation= user['activation']
        balance = user['balance_checking']
        overdrafts = 0
        if activation == 'deactivate' and balance >= 0:
            for info in user:
                if info == 'activation':
                    user.update({info:'activate'})
                if info == 'overdrafts':
                    user.update({info:0})
            self.update_customer(user)
            print('Thank you for settling The outstanding dues. The account has been reactivated and is now fully operational')


    def generate_report(self):
        id_file= self.customers.get("account_id")+'_statement.txt'
        self.get_transaction_hisory()
        try:
            with open(id_file, 'w',encoding="utf-8" ) as file:
                file.write(f'Welcome {self.customers.get("first_name")}👋\nAccount ID: {self.customers['account_id']}               First Name: {self.customers['first_name']}                 Last Name: {self.customers['last_name']}             Password: {self.customers['password']} \nBalance Checking: {self.customers['balance_checking']}       Balance_Savings: {self.customers['balance_savings']}        Times of Overdrafts: {self.customers['overdrafts']}      Activation state: {self.customers['activation']}')
                file.write('\nYour Recent Transactions:\n')
                for row in self.all_transactions:
                    file.write(f'{row}\n')
        except FileNotFoundError:
            print(f'Sorry  file not found:(')


    def get_transaction_hisory(self):
        try:
            with open(self.customers.get("account_id")+'.csv', "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    # print(row)
                    self.all_transactions.append(row)
                return self.all_transactions
        except FileNotFoundError:
            print(f'Sorry, file not found:(')


    def print_transaction_hisory(self):
        self.get_transaction_hisory()
        for row in self.all_transactions:
            print(row)


    def save_transaction(self):
        id_file= self.customers.get("account_id")+'.csv'
        try:
            with open(id_file, 'x',newline="" ) as file:
                fieldnames =['transaction_id','date','time','type','amount','account','balance']
                writer = csv.DictWriter(file, fieldnames= fieldnames)
                writer.writeheader()
        except FileExistsError:
            pass

        try:
            with open(id_file, 'a',newline="" ) as file:
                fieldnames =['transaction_id','date','time','type','amount','account','balance']
                writer = csv.DictWriter(file, fieldnames= fieldnames)
                writer.writerow({
                    'transaction_id':self.transaction.get('transaction_id'), 
                    'date': self.transaction.get('date'),
                    'time': self.transaction.get('time'),
                    'type': self.transaction.get('type'),
                    'amount': self.transaction.get('amount'),
                    'account': self.transaction.get('account'),
                    'balance':self.transaction.get('balance'),
                    })
        except FileNotFoundError:
            print(f'Sorry  file not found:(')


    def update_transaction(self,type, amount, account, balance):
        timedate=datetime.datetime.now()
        id = str(uuid.uuid4())
        id = id[0:8]
        self.transaction.update({'transaction_id':id ,
                                'date': timedate.date() ,
                                'time': timedate.time().strftime('%X')+' '+ timedate.strftime("%p"),
                                'type': type,
                                'amount': amount,
                                'account': account,
                                'balance':balance})
        # print(self.transaction.items())
        self.save_transaction()


    def withdraw_from_checking(self, price):
            done = False
            
            price = int(price)
            if self.islogin == False:
                raise UseeIsNOTlogin
            else:
                activation= self.customers['activation']
                if activation == 'activate':
                    current_balance_checking =float(self.customers.get("balance_checking"))
                    if price > current_balance_checking:
                        new_balance_checking = self.overdraft_Protection(current_balance_checking , price)
                        if new_balance_checking < current_balance_checking:
                            for info in self.customers:
                                if info == 'balance_checking':
                                    self.customers.update({info:new_balance_checking })
                            self.update_customer( self.customers)
                            self.update_transaction('withdraw', '-'+str(price), 'checking', new_balance_checking)
                            print(f'A {price} have been withdraw from your checking account successfully and your current checking balnce is {new_balance_checking}$')                        

                        else:
                            pass

                    elif price > 0 and price <= current_balance_checking :
                        current_balance_checking -= price
                        self.customers.get("balance_checking")
                        for info in self.customers:
                            if info == 'balance_checking':
                                self.customers.update({info:current_balance_checking })
                        self.update_customer( self.customers)
                        self.update_transaction('withdraw', '-'+str(price), 'checking', current_balance_checking)

                        print(f'A {price} have been withdraw from your checking account successfully and your current checking balnce is {current_balance_checking}$')                        
                    else:
                        raise ValueError
                else:
                    raise Deactivate('your accout is deactivated')


    def withdraw_from_savings(self, price):
            price = int(price)
            if self.islogin == False:
                raise UseeIsNOTlogin
            else:
                # for info in self.customers:
                current_balance_savings =float(self.customers.get("balance_savings"))
                if price>= current_balance_savings:
                    print(f'Sorry The transaction could not be processed because the account does not have sufficient balance of {current_balance_savings}$')
                    raise Declined
                elif price > 0:
                    current_balance_savings -= price
                    self.customers.get("balance_savings")
                    for info in self.customers:
                        if info == 'balance_savings':
                            self.customers.update({info:current_balance_savings })
                    # print(self.customers)
                    # self.customers
                    self.update_customer( self.customers)
                    self.update_transaction('withdraw', '-'+str(price), 'Savings', current_balance_savings)
                    print(f'A {price} have been withdraw from your checking account successfully and your current Savings balnce is {current_balance_savings}$')                        

                else:
                    raise ValueError


    def deposit_into_savings(self, amount):
        amount = int(amount)
        if self.islogin == False:
                raise UseeIsNOTlogin
        else:
            if amount < 1:
                raise ValueError
            else:
                new_balance_savings =float(self.customers.get("balance_savings"))
                new_balance_savings += amount
                self.customers.get("balance_savings")
                for info in self.customers:
                    if info == 'balance_savings':
                        self.customers.update({info:new_balance_savings })
                # print(self.customers)
                # self.customers
                self.update_customer( self.customers)
                self.update_transaction('Deposit', '+'+str(amount), 'Savings', new_balance_savings)
                print(f'A {amount} have been Deposit to your Savings account successfully and your current Savings balnce is {new_balance_savings}$')                        


    def deposit_into_checking(self, amount):
        amount = int(amount)
        if self.islogin == False:
            raise UseeIsNOTlogin
        else:
            if amount < 1:
                raise ValueError
            else:
                new_balance_checking =float(self.customers.get("balance_checking"))
                new_balance_checking += amount
                self.customers.get("balance_checking")
                for info in self.customers:
                    if info == 'balance_checking':
                        self.customers.update({info:new_balance_checking })
                # print(self.customers)
                # self.customers
                self.update_customer( self.customers)
                self.update_transaction('Deposit', '+'+str(amount), 'Checking', new_balance_checking)
                print(f'A {amount} have been Deposit from your checking account successfully and your current Checking balnce is {new_balance_checking}$')  
                self.reactivate(self.customers)


    def transfer_from_savings_to_checking(self, amount):
        amount = int(amount)
        if self.islogin == False:
            raise UseeIsNOTlogin
        else:
            if amount < 1:
                raise ValueError
            else:
                current_balance_savings =float(self.customers.get("balance_savings"))
                if amount>= current_balance_savings:
                    print(f'Sorry The transaction could not be processed because the account does not have sufficient balance of {current_balance_savings}$')
                    raise Declined
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
                    self.update_transaction('Transfer', '-'+str(amount), 'Savings', current_balance_savings)
                    self.update_transaction('Transfer', '+'+str(amount), 'Checking',new_balance_checking)
                    print(f'A {amount} have been Transfered from your Savings account to checking account successfully and your current Savings balnce is {current_balance_savings}$')                        
                    self.reactivate(self.customers)
                else:
                    raise ValueError


    def transfer_from_checking_to_savings(self, amount):
        amount = int(amount)
        if self.islogin == False:
            raise UseeIsNOTlogin
        else:
            activation= self.customers['activation']
            if activation == 'activate':
                if amount < 1:
                    raise ValueError
                else:
                    current_balance_checking =float(self.customers.get("balance_checking"))
                    current_balance_savings =float(self.customers.get("balance_savings"))
                    if amount>= current_balance_checking:
                        new_balance_checking = self.overdraft_Protection(current_balance_checking , amount)
                        if new_balance_checking < current_balance_checking:
                            current_balance_savings += amount
                            for info in self.customers:
                                if info == 'balance_savings':
                                    self.customers.update({info:current_balance_savings })
                                if info == 'balance_checking':
                                    self.customers.update({info:new_balance_checking })
                            self.update_customer( self.customers)
                            self.update_transaction('Transfer', '-'+str(amount), 'Checking',current_balance_checking)
                            self.update_transaction('Transfer', '+'+str(amount), 'Savings', current_balance_savings)
                            print(f'A {amount} have been Transfered from your checking account to your Savings account successfully and your current checking balnce is {current_balance_checking}$')                        

                        else:
                            pass
                    elif amount > 0:
                        current_balance_checking -= amount
                        current_balance_savings += amount
                        # self.customers.get("balance_savings")
                        for info in self.customers:
                            if info == 'balance_savings':
                                self.customers.update({info:current_balance_savings })
                            if info == 'balance_checking':
                                self.customers.update({info:current_balance_checking })
                            
                        # print(self.customers)
                        # self.customers
                        self.update_customer( self.customers)
                        self.update_transaction('Transfer', '-'+str(amount), 'Checking',current_balance_checking)
                        self.update_transaction('Transfer', '+'+str(amount), 'Savings', current_balance_savings)
                        print(f'A {amount} have been Transfered from your checking account to your Savings account successfully and your current checking balnce is {current_balance_checking}$')                        

                    else:
                        raise ValueError
            else:
                raise Deactivate


    def transfer_checking_to_another_account(self, amount, user_account_id):
        users=[]
        user={}
        userfound= False
        amount = int(amount)
        if self.islogin == False:
            raise UseeIsNOTlogin
        else:
            activation= self.customers['activation']
            if activation == 'activate':
                if amount < 1:
                    raise ValueError
                else:
                    users= self.get_customers()
                    for line in users:
                        if user_account_id in line['account_id']:
                            user.update(line)
                            userfound= True
                            break
                    if userfound == False:    
                        raise IdNotFound('There Is No Account With This ID')
                    customer_balance_checking =float(self.customers.get("balance_checking"))
                    user_checking =float(user.get("balance_checking"))
                    if amount>= customer_balance_checking:
                        new_balance_checking = self.overdraft_Protection(customer_balance_checking , amount)
                        if new_balance_checking < customer_balance_checking:
                            user_checking += amount
                            for info in self.customers:
                                if info == 'balance_checking':
                                    self.customers.update({info:new_balance_checking })
                            for info in user:
                                if info == 'balance_checking':
                                    user.update({info:user_checking })
                                    break
                            self.update_customer(user)
                            self.update_customer( self.customers)
                            self.update_transaction(f'Transfer to {user.get("account_id")}', '-'+str(amount), 'Checking',new_balance_checking)
                            print(f'A {amount} have been Transfered from your checking account to your {user_account_id} account successfully and your current checking balnce is {new_balance_checking}$')                        

                        else:
                            pass
                    else:
                        customer_balance_checking -= amount
                        
                        user_checking += amount
                        for info in self.customers:
                            if info == 'balance_checking':
                                self.customers.update({info:customer_balance_checking })
                                break
                        self.update_customer( self.customers)
                        
                        for info in user:
                            if info == 'balance_checking':
                                user.update({info:user_checking })
                                # print(user)
                                break
                        self.update_customer(user)
                        self.update_transaction(f'Transfer to {user.get("account_id")}', '-'+str(amount), 'Checking',customer_balance_checking)
                        print(f'A {amount} have been Transfered from your checking account to {user['first_name']}\' account successfully and your current checking balnce is {customer_balance_checking}$')                        
                        self.reactivate(user)
            else:
                raise Deactivate


    def transfer_savings_to_another_account(self, amount, user_account_id):
        users=[]
        user={}
        userfound = False
        amount = int(amount)
        if self.islogin == False:
            raise UseeIsNOTlogin
        else:
            activation= self.customers['activation']
            if activation == 'activate':
                if amount < 1:
                    raise ValueError

                else:
                    users= self.get_customers()
                    for line in users:
                        if user_account_id in line['account_id']:
                            user.update(line)
                            userfound= True
                            break
                    if userfound == False:
                        raise IdNotFound('There Is No Account With This ID')
                    customer_balance_savings =float(self.customers.get("balance_savings"))
                    if amount>= customer_balance_savings:
                        print(f'Sorry The transaction could not be processed because the account does not have sufficient balance of {customer_balance_savings}$')
                        raise Declined
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
                        self.update_transaction(f'Transfer to {user.get("account_id")}', '-'+str(amount), 'Savings',customer_balance_savings)
                        print(f'A {amount} have been Transfered from your Savings account to your {user_account_id} account successfully and your current checking balnce is {customer_balance_savings}$')                        
                        self.reactivate(user)
            else:
                print(f'your account is deactivated due to your over overdrafts \nKindly settle your outstanding balance. The amount credited to your account is {self.customers['balance_checking']}')


    


bank = Bank('bank.csv')
# 

# bank.add_customer(Customer('sara', 'aaaa',"jjj" , 20000, 5000))
# print(bank.get_id())
# ctr=Customer('Rama', 'Khalid', 'Rama123', 20000, 5000)
bank.top_customer()
new_account =Account('bank.csv')
print(new_account.login( '10013', 'meme@1234'))
new_account.customer_info()
# print(bank.get_customers())
# new_account.generate_report()
# new_account.get_id()
# # new_account.deposit_into_checking(500)
# # new_account.deposit_into_savings(500)
# new_account.withdraw_from_checking(20)
# new_account.withdraw_from_checking(10)
# new_account.withdraw_from_checking(20)
# # new_account.withdraw_from_savings(80)
# new_account.transfer_from_savings_to_checking(20)
# new_account.transfer_from_checking_to_savings(20)
# new_account.transfer_savings_to_another_account(100, '10005' )
# new_account.transfer_checking_to_another_account(100, '10005' )
# new_account.print_transaction_hisory()
# new_account.open_transaction_file()
# bank.update_customer()
# print(new_account.customers)
# print(Customer.id)
# print(bank.get_customers())
# print(new_account.customer_info())