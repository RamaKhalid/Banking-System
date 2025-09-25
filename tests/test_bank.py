import unittest
from bank.bank import *
from bank.exceptions import*

class TestBanck(unittest.TestCase):
    def setUp(self):
        self.bank = Bank('bank.csv')
        self.users =bank.get_customers()
        

    def test_creating_bank_object(self):
        self.assertEqual(self.bank.file,'bank.csv' )


    # def test_get_customers(self):
    #     self.assertEqual(bank.get_customers(),[{'account_id': '10001', 'first_name': 'suresh', 'last_name': 'sigera', 'password': 'juagw362', 'balance_checking': '1000', 'balance_savings': '10000', 'overdrafts': '0', 'activation': 'activate'}, {'account_id': '10002', 'first_name': 'james', 'last_name': 'taylor', 'password': 'idh36%@#FGd', 'balance_checking': '10000', 'balance_savings': '10000', 'overdrafts': '0', 'activation': 'activate'}, {'account_id': '10003', 'first_name': 'Rama', 'last_name': 'Khalid', 'password': 'Rama123', 'balance_checking': '0.0', 'balance_savings': '1000.0', 'overdrafts': '0', 'activation': 'activate'}, {'account_id': '10004', 'first_name': 'stacey', 'last_name': 'abrams', 'password': 'DEU8_qw3y72$', 'balance_checking': '2000', 'balance_savings': '20000', 'overdrafts': '0', 'activation': 'activate'}, {'account_id': '10005', 'first_name': 'jake', 'last_name': 'paul', 'password': 'd^dg23g)@', 'balance_checking': '120000.0', 'balance_savings': '100000', 'overdrafts': '0', 'activation': 'activate'}, {'account_id': '10006', 'first_name': 'sara', 'last_name': 'aaaa', 'password': '1221', 'balance_checking': '20304.0', 'balance_savings': '5000', 'overdrafts': '0', 'activation': 'activate'}, {'account_id': '10007', 'first_name': 'Reema', 'last_name': 'sss', 'password': 'reemmee111', 'balance_checking': '222222', 'balance_savings': '1111', 'overdrafts': '0', 'activation': 'activate'}, {'account_id': '10008', 'first_name': 'jojo', 'last_name': 'koko', 'password': 'kokojojo', 'balance_checking': '90000', 'balance_savings': '2', 'overdrafts': '0', 'activation': 'activate'}])

    def test_adding_new_customer(self):
        id=[]
        with open('bank.csv', 'r', encoding='utf-8') as f:
            # rows = sum(1 for line in f)
            for line in f:
                id= line[0:5]
        id = int(id)
        
        with open('bank.csv', 'r', encoding='utf-8') as f:
            rows = sum(1 for line in f)
        self.bank.add_customer(Customer('sara', 'ahmed',"sara1234" , 20000, 5000))
        with open('bank.csv', 'r', encoding='utf-8') as f:
            total_rows = sum(1 for line in f)
        #check id is sequential
        self.assertEqual(self.bank.get_id() , id+1)
        #check if new customer has been added to the csv file
        self.assertEqual(total_rows,rows+1 )
    
    