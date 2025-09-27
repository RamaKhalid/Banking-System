import unittest                   
from bank.bank import *
from bank.exceptions import*
from unittest import mock
from unittest.mock import patch

class TeatOverdraftFee(unittest.TestCase):
    def setUp(self):
        self.bank = Bank('bank.csv')
        self.new_account =Account('bank.csv')
        self.customers=[]
        
    @mock.patch('builtins.input', side_effect=['Y'])
    def test_overdraft_Protection_applying_fee(self, mock_input):
        #login
        self.new_account.login('10007', 'reemmee111' )
        # retrieve balance_checking befor withdraw
        balance_checking = float(self.new_account.customers.get('balance_checking'))
        self.new_account.withdraw_from_checking(220233)
        # retrieve balance_checking after withdraw
        new_balance_checking = float(self.new_account.customers.get('balance_checking'))

        #compare the result
        self.assertEqual(new_balance_checking, balance_checking-220233 -35 )

        mock_input.assert_called_once_with('To continue Enter Y or N to stop: ')


    @mock.patch('builtins.input', side_effect=['N', 'n'])
    def test_overdraft_Protection_when_Transiction_stops(self, mock_input):
        #login
        self.new_account.login('10006', '1221' )
        # retrieve balance_checking befor withdraw
        balance_checking = float(self.new_account.customers.get('balance_checking'))
        self.new_account.withdraw_from_checking(20305)
        # retrieve balance_checking after withdraw
        new_balance_checking = float(self.new_account.customers.get('balance_checking'))
        #compare the result
        self.assertEqual(new_balance_checking, balance_checking )

        mock_input.assert_called_once_with('To continue Enter Y or N to stop: ')

    @patch('builtins.print')
    def test_overdraft_Protection_when_Transiction_Exceeds_limit(self, mock_print):
        #login
        self.new_account.login('10002', 'idh36%@#FGd' )
        self.new_account.withdraw_from_checking(10100)
        mock_print.assert_called_with('Sorry You can\'t Do This Transaction as it will Exceeds the minimum limit allowed with the fee (less than $-100)')

