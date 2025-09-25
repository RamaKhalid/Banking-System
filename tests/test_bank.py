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
        # Test if user withdraw with negative number
        with self.assertRaises(Declined):
            self.new_account.withdraw_from_savings(float(self.new_account.customers.get('balance_savings'))+ 100 )
        # retrieve balance_asvings befor withdraw
        balance_savings= float(self.new_account.customers.get('balance_savings'))
        self.new_account.withdraw_from_savings(10)
        # retrieve balance_asvings befor withdraw
        new_balance_savings= float(self.new_account.customers.get('balance_savings'))
        #compare the result
        self.assertEqual( new_balance_savings, balance_savings-10 )

    def test_deposit_into_saving(self):
        # Test if user Deposit without login
        with self.assertRaises(UseeIsNOTlogin):
            self.new_account.deposit_into_savings(20)
        
