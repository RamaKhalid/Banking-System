import unittest                   
from bank.bank import *
from bank.exceptions import*

class TestBanck(unittest.TestCase):
    def setUp(self):
        self.bank = Bank('bank.csv')
        self.users =bank.get_customers()
        

    def test_creating_bank_object(self):
        self.assertEqual(self.bank.file,'bank.csv' )

    def test_adding_new_customer(self):
        id = 0
        #Get this code from conor
        with open('bank.csv', 'r', encoding='utf-8') as f:
            rows = sum(1 for line in f)
        with open('bank.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                id = max(id, int(row['account_id']))
        
        self.bank.add_customer(Customer('sara', 'ahmed',"sara1234" , 20000, 5000))
        with open('bank.csv', 'r', encoding='utf-8') as f:
            total_rows = sum(1 for line in f)
        #check id is sequential
        self.assertEqual(self.bank.get_id() , id+1)
        #check if new customer has been added to the csv file
        self.assertEqual(total_rows, rows+1 )
    


class TestAccountClass (unittest.TestCase):
    def setUp(self):
        self.bank = Bank('bank.csv')
        self.new_account =Account('bank.csv')
        self.customers=[]

    def test_user_login(self):
        #Test when both ID and Password is wrong 
        with self.assertRaises(UseeIsNOTlogin):
            self.new_account.login('2345', '0000' )
        #Test when The Password is wrong 
        with self.assertRaises(UseeIsNOTlogin):
            self.new_account.login('10003', '0000' )
        #Test when The ID is wrong 
        with self.assertRaises(UseeIsNOTlogin):
            self.new_account.login('2345', 'Rama123' )
        #Test When login with the right data
        self.allUsers= self.new_account.get_customers()
        for info in self.allUsers:
            self.new_account.customers =info
        self.assertEqual(self.new_account.login('10003', 'Rama123' ), f'Welcome {self.new_account.customers['first_name']}👋, you have been loged in successfully🎉 ')
    

    def test_withdraw_from_checking(self):
        # Test if user withdraw without login
        with self.assertRaises(UseeIsNOTlogin):
            self.new_account.withdraw_from_checking(20)
        #login
        self.new_account.login('10003', 'Rama123' )
        with self.assertRaises(ValueError):
            self.new_account.withdraw_from_checking(-29)
        # retrieve balance_checking befor withdraw
        balance_checking = float(self.new_account.customers.get('balance_checking'))

        self.new_account.withdraw_from_checking(10)
        # retrieve balance_checking after withdraw
        new_balance_checking = float(self.new_account.customers.get('balance_checking'))

        #compare the result
        self.assertEqual(new_balance_checking, balance_checking-10 )

        # with self.assertRaises(Deactivate):
        #     self.new_account.customers.update({'activation':'deactivate' })
        #     self.new_account.update_customer( self.new_account.customers)
        #     self.new_account.withdraw_from_checking(29)
        # self.new_account.customers.update({'activation':'activate' })
        # self.new_account.update_customer( self.new_account.customers)

    def test_withdraw_from_savings(self):
        # Test if user withdraw without login
        with self.assertRaises(UseeIsNOTlogin):
            self.new_account.withdraw_from_savings(20)
        #login
        self.new_account.login('10003', 'Rama123' )
        with self.assertRaises(ValueError):
            self.new_account.withdraw_from_savings(-29)
        # Test if user withdraw More than they have
        with self.assertRaises(Declined):
            self.new_account.withdraw_from_savings(float(self.new_account.customers.get('balance_savings'))+ 100 )
        # retrieve balance_asvings befor withdraw
        balance_savings= float(self.new_account.customers.get('balance_savings'))
        self.new_account.withdraw_from_savings(10)
        # retrieve balance_asvings after withdraw
        new_balance_savings= float(self.new_account.customers.get('balance_savings'))
        #compare the result
        self.assertEqual( new_balance_savings, balance_savings-10 )

    def test_deposit_into_savings(self):
        # Test if user Deposit without login
        with self.assertRaises(UseeIsNOTlogin):
            self.new_account.deposit_into_savings(20)
        #login
        self.new_account.login('10003', 'Rama123' )
        # Test if user Deposit with negative number
        with self.assertRaises(ValueError):
            self.new_account.deposit_into_savings(-29)

        # retrieve balance_asvings befor withdraw
        balance_savings= float(self.new_account.customers.get('balance_savings'))
        self.new_account.deposit_into_savings(20)
        # retrieve balance_asvings afet withdraw
        new_balance_savings= float(self.new_account.customers.get('balance_savings'))
        #compare the result
        self.assertEqual( new_balance_savings, balance_savings+20 )


    def test_deposit_into_Checking(self):
        # Test if user Deposit without login
        with self.assertRaises(UseeIsNOTlogin):
            self.new_account.deposit_into_checking(20)
        #login
        self.new_account.login('10003', 'Rama123' )
        # Test if user Deposit with negative number
        with self.assertRaises(ValueError):
            self.new_account.deposit_into_checking(-29)

        # retrieve balance_asvings befor withdraw
        balance_checking= float(self.new_account.customers.get('balance_checking'))
        self.new_account.deposit_into_checking(20)
        # retrieve balance_asvings after withdraw
        new_balance_checking= float(self.new_account.customers.get('balance_checking'))
        #compare the result
        self.assertEqual( new_balance_checking, balance_checking +20 )

    
    def test_transfer_from_savings_to_checking(self):
        # Test if user transfer without login
        with self.assertRaises(UseeIsNOTlogin):
            self.new_account.transfer_from_savings_to_checking(20)
        #login
        self.new_account.login('10003', 'Rama123' )
        # Test if user transfer with negative number
        with self.assertRaises(ValueError):
            self.new_account.transfer_from_savings_to_checking(-29)
        # Test if user transfer More than they have
        with self.assertRaises(Declined):
            self.new_account.transfer_from_savings_to_checking(float(self.new_account.customers.get('balance_savings'))+ 100 )

        balance_checking= float(self.new_account.customers.get('balance_checking'))
        balance_savings= float(self.new_account.customers.get('balance_savings'))
        self.new_account.transfer_from_savings_to_checking(20)
        new_balance_savings= float(self.new_account.customers.get('balance_savings'))
        new_balance_checking= float(self.new_account.customers.get('balance_checking'))
        self.assertEqual( new_balance_checking, balance_checking +20 )
        self.assertEqual( new_balance_savings, balance_savings-20 )


    def test_transfer_from_checking_to_savings(self):
        # Test if user transfer without login
        with self.assertRaises(UseeIsNOTlogin):
            self.new_account.transfer_from_checking_to_savings(20)
        #login
        self.new_account.login('10003', 'Rama123' )
        # Test if user transfer with negative number
        with self.assertRaises(ValueError):
            self.new_account.transfer_from_checking_to_savings(-29)

        balance_checking= float(self.new_account.customers.get('balance_checking'))
        balance_savings= float(self.new_account.customers.get('balance_savings'))
        self.new_account.transfer_from_checking_to_savings(20)
        new_balance_savings= float(self.new_account.customers.get('balance_savings'))
        new_balance_checking= float(self.new_account.customers.get('balance_checking'))
        self.assertEqual( new_balance_checking, balance_checking -20 )
        self.assertEqual( new_balance_savings, balance_savings+20 )


    def test_transfer_checking_to_another_account(self):
        # Test if user transfer without login
        with self.assertRaises(UseeIsNOTlogin):
            self.new_account.transfer_checking_to_another_account(20, '10004')
        #login
        self.new_account.login('10003', 'Rama123' )
        # Test if user transfer with negative number
        with self.assertRaises(ValueError):
            self.new_account.transfer_checking_to_another_account(-29, '10004')
        # Test if user transfer with wrong ID
        with self.assertRaises(IdNotFound):
            self.new_account.transfer_checking_to_another_account(29, '1004')

        # retrieve balance_checking befor get transfers
        balance_checking= float(self.new_account.customers.get('balance_checking'))
        # retrieve the other account balance_checking befor get transfers
        user ={}
        with open('bank.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if '10004' in row['account_id']:
                    user.update(row)
        user_balance_checking= float(user.get('balance_checking'))

        self.new_account.transfer_checking_to_another_account(30, '10004')

        # retrieve balance_checking after get transfers
        new_balance_checking= float(self.new_account.customers.get('balance_checking'))
        # retrieve the other account balance_checking afet get transfers
        new_user ={}
        with open('bank.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if '10004' in row['account_id']:
                    new_user.update(row)
        new_user_balance_checking= float(new_user.get('balance_checking'))

        self.assertEqual(new_user_balance_checking, user_balance_checking+30 )
        self.assertEqual(balance_checking-30 , new_balance_checking )


    def test_transfer_savings_to_another_account(self):
        # Test if user transfer without login
        with self.assertRaises(UseeIsNOTlogin):
            self.new_account.transfer_savings_to_another_account(20, '10004')
        #login
        self.new_account.login('10003', 'Rama123' )
        # Test if user transfer with negative number
        with self.assertRaises(ValueError):
            self.new_account.transfer_savings_to_another_account(-29, '10004')
        # Test if user transfer with wrong ID
        with self.assertRaises(IdNotFound):
            self.new_account.transfer_savings_to_another_account(29, '1004')

        # retrieve balance_checking befor get transfers
        balance_savings= float(self.new_account.customers.get('balance_savings'))
        # retrieve the other account balance_checking befor get transfers
        user ={}
        with open('bank.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if '10004' in row['account_id']:
                    user.update(row)
        user_balance_checking= float(user.get('balance_checking'))

        self.new_account.transfer_savings_to_another_account(30, '10004')

        # retrieve balance_checking after get transfers
        new_balance_savings= float(self.new_account.customers.get('balance_savings'))
        # retrieve the other account balance_checking afet get transfers
        new_user ={}
        with open('bank.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if '10004' in row['account_id']:
                    new_user.update(row)
        new_user_balance_checking= float(new_user.get('balance_checking'))

        self.assertEqual(new_user_balance_checking, user_balance_checking+30 )
        self.assertEqual(balance_savings-30 , new_balance_savings )


        


