from abc import ABC, abstractmethod
from datetime import datetime

class Account(ABC):
    """
    abstract base class for all the accounts type.
    adheres to the single responsibilty Principle (SRP) by only handling generic account operations.
    """
    
    def __init__(self,account_number, balance = 0.0):
        self._account_number = account_number
        self._balance = balance
        self._is_locked = False
        self.transaction_history = []
    
    @property
    def balance(self):
        return self._balance
    
    @ property
    def account_number(self):
        return self._account_number
    
    def deposit(self,amount):
        if self._is_locked:
            raise Exception("Account is locked. cannot perform operations")
        if amount>0:
            self._balance += amount
            self.transaction_history.append(
                {'type':'Deposit','amount':amount,'date':datetime.now(),'balance':self._balance}
            )
        else:
            raise ValueError('Deposit amount must be positive.')
        
    def withdraw(self,amount):
        if self._is_locked:
            raise Exception("Account is locked. cannnot perform operations")
        if amount > 0 and amount<=self._balance:
            self._balance -= amount
            self.transaction_history.append(
                {
                    'type':'withdraw', 'amount':amount,'date':datetime.now(),'balance':self._balance
                }
            )
        else:
            Exception('Insufficient funds or invalid input.')
    def lock_account(self):
        self._is_locked = True
    def unlock_account(self):
        self._is_locked = False
    def show_transcation_history(self):
        if not self.transaction_history:
            print("No transcations found")
            return 
        for transaction in self.transaction_history:
            print(
                f"{transaction['type']} of {transaction['amount']} on {transaction['date']}. Balance : {transaction['balance']}"
            )
                 
    @abstractmethod
    def calculate_interest(self):
        """
            Abstract method ensures that the subclasses implement specific interest calculation logic.
            adheres to the open/close principle (OCP) by allowing multiple extensions for new account types without modifying this class. 
        """
        pass
    
    
    