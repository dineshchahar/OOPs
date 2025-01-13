from .account import Account
from datetime import datetime

class CurrentAccount(Account):
    """
        Represents a current account with overdraft capability.
        Adheres  to LSP by overriding the 'withdraw' method with extended behaviour for overdrafts.
         
    """
    
    def __init__(self, account_number, balance=0,overdraft_limit = 1000.0):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if self._is_locked:
            raise Exception("Account is locked. Cannot perform Operations.")
        if amount> 0 and (self._balance + self.overdraft_limit) >= amount:
            self._balance -= amount
            self.transaction_history.append(
                {'type':'withdrawal','amount':amount,'date':datetime.now(), 'balance':self._balance}
            )
        else:
            raise Exception("Exceeded overdraft limit or invalid input")
        
    def calculate_interest(self):
        """
            current accounts do not accure interest.
            This impplementation satisfies the abstract method requirement.
             
        """
        return 0