import csv


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

    
    account_id =10006
    
    def __init__(self,first_name, last_name, password, balance_checking, balance_savings):
        self.account_id = Customer.id
        self.first_name =first_name
        self.last_name =last_name
        self.password =password
        self.balance_checking =balance_checking
        self.balance_savings =balance_savings
        Customer.account_id += 1
        self.overdrafts = 0
        self.activation= 'activate'

    def info(self):
        return(f'First Name: {self.first_name} \nLast Name: {self.last_name} \nPassword: {self.password} \nBalance Checking: {self.balance_checking} \nBalance_Savings: {self.balance_savings}')

    
class Bank():
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
                fieldnames =['account_id', 'first_name', 'last_name', 'password', 'balance_checking', 'balance_savings', 'overdrafts','activation']
                writer = csv.DictWriter(file, fieldnames= fieldnames)
                writer.writerows({
                    'account_id':info.account_id, 
                    'first_name': info.first_name ,
                    'last_name': info.last_name,
                    'password': info.password,
                    'balance_checking': info.balance_checking,
                    'balance_savings': info.balance_savings,
                    'overdrafts':0,
                    'activation': 'activate'
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
            fieldnames =['account_id', 'first_name', 'last_name', 'password', 'balance_checking', 'balance_savings','overdrafts','activation']
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
                'activation': info['activation']
            } 
                for info in list)

    def add_customer(self,customer):
        self.customers.append(customer)
        self.save() 

    def customer_info(self ):
        for i in self.customers:
            return (f'Account_id: {i.account_id} \nFirst Name: {i.first_name} \nLast Name: {i.last_name} \nPassword: {i.password} \nBalance Checking: {i.balance_checking} \nBalance_Savings: {i.balance_savings} \nOverdrafts {i.overdrafts} \nActivation {i.activation}')

        

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
                    if line['account_id'] == data['account_id']:
                        # print(line)
                        line.update(data)
                        # print(line)
                # print(users)
                self.save_update(users)




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
                    print(f'Welcome {info['first_name']}👋, you have been loged in successfully🎉 ')
                # else:
                #     print('User Not found please check your Password')
        if idFound == False or self.islogin==False :
            print('User Not found please check your ID or password')

        

    def overdraft_Protection(self, balance, amount):
        new_balance =float(balance)
        new_balance -= amount
        if new_balance < -100:
            print('Sorry You can\'t Do This Transaction as you Exceeds the minimum limit allowed (less than -100$)' )
            return balance
        elif balance>=0 and new_balance<0:
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
            if charge == 'N':
                print('Your Transaction is stoped')
                return balance
        elif balance <0 and new_balance>= -100:
            self.overdrafts_count()
            return new_balance


    def overdrafts_count(self):
        overdrafts = self.customers['overdrafts']
        overdrafts = int(overdrafts)
        if overdrafts== 2:
            print('you over overdrafts U_U Your account will be deactivate ^3^')
            deactivate = 'deactivate'
            for info in self.customers:
                if info == 'activation':
                    self.customers.update({info:deactivate})
        else:
            overdrafts +=1
            for info in self.customers:
                if info == 'overdrafts':
                    self.customers.update({info:overdrafts})



#ADD THE Overdraft Protection 
    def withdraw_from_checking(self, price):
            done = False
            # HANNDEL THIS ERROR*********************
            price = int(price)
            if self.islogin == False:
                # raise loginError
                print('please login first')
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
                        else:
                            pass

                    elif price > 0 and price <= current_balance_checking :
                        current_balance_checking -= price
                        self.customers.get("balance_checking")
                        for info in self.customers:
                            if info == 'balance_checking':
                                self.customers.update({info:current_balance_checking })
                        self.update_customer( self.customers)
                        print(f'A {price} have been withdraw from your checking account successfully and your current checking balnce is {current_balance_checking}$')                        
                    else:
                        print('number must be >0')
                else:
                    print(f'your account is deactivated due to your over overdrafts \nKindly settle your outstanding balance. The amount credited to your account is {self.customers['balance_checking']}')


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
        if self.islogin == False:
            # raise loginError
            print('please login first')
        else:
            activation= self.customers['activation']
            if activation == 'activate':
                if amount < 1:
                    pass
                    # raise error
                else:
                    current_balance_checking =float(self.customers.get("balance_checking"))
                    if amount>= current_balance_checking:
                        new_balance_checking = self.overdraft_Protection(current_balance_checking , amount)
                        if new_balance_checking < current_balance_checking:
                            for info in self.customers:
                                if info == 'balance_checking':
                                    self.customers.update({info:new_balance_checking })
                            self.update_customer( self.customers)
                        else:
                            pass
                    elif amount > 0:
                        current_balance_checking -= amount
                        current_balance_savings =float(self.customers.get("balance_savings"))
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
                    else:
                        print('number must be >0')
            else:
                print(f'your account is deactivated due to your over overdrafts \nKindly settle your outstanding balance. The amount credited to your account is {self.customers['balance_checking']}')


    def transfer_checking_to_another_account(self, amount, user_account_id):
        users=[]
        user={}
        amount = int(amount)
        if self.islogin == False:
            # raise loginError
            print('please login first')
        else:
            activation= self.customers['activation']
            if activation == 'activate':
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
                        new_balance_checking = self.overdraft_Protection(customer_balance_checking , amount)
                        if new_balance_checking < customer_balance_checking:
                            for info in self.customers:
                                if info == 'balance_checking':
                                    self.customers.update({info:new_balance_checking })
                            self.update_customer( self.customers)
                        else:
                            pass
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
            else:
                print(f'your account is deactivated due to your over overdrafts \nKindly settle your outstanding balance. The amount credited to your account is {self.customers['balance_checking']}')


    def transfer_savings_to_another_account(self, amount, user_account_id):
        users=[]
        user={}
        amount = int(amount)
        if self.islogin == False:
            # raise loginError
            print('please login first')
        else:
            activation= self.customers['activation']
            if activation == 'activate':
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
            else:
                print(f'your account is deactivated due to your over overdrafts \nKindly settle your outstanding balance. The amount credited to your account is {self.customers['balance_checking']}')





bank = Bank('bank.csv')
# 

# bank.add_customer(Customer('sara', 'aaaa',"jjj" , 20000, 5000))
# ctr=Customer('Rama', 'Khalid', 'Rama123', 20000, 5000)

new_account =Account('bank.csv')
# new_account.login( '10003', 'fffff')
# # new_account.deposit_into_checking(500)
# # new_account.deposit_into_savings(500)
# new_account.withdraw_from_checking(20)
# # new_account.withdraw_from_savings(80)
# # new_account.transfer_from_savings_to_checking(20)
# # new_account.transfer_from_checking_to_savings(20)
# new_account.transfer_savings_to_another_account(2000, '10005' )
# bank.update_customer()
# print(new_account.customers)
# print(Customer.id)
# print(bank.get_customers())
# print(bank.customer_info())
