from accounts.saving_account import SavingAccount
from accounts.current_account import CurrentAccount
from accounts.Business_account import BusinessAccount

from Customer import Customer
from Bank import Bank

if __name__=="__main__":
    
    bank = Bank("Mybank")
    Customer1 = Customer(1,'Alice')
    Customer2 = Customer(2,'Bob')

    bank.add_customer(Customer1)
    bank.add_customer(Customer2)
    
    savings = SavingAccount('S1001',5000)
    current = CurrentAccount('C1002',2000,overdraft_limit=1000)
    business = BusinessAccount('B1003',10000)
    
    
    Customer1.add_account(savings)
    Customer1.add_account(current)
    Customer2.add_account(business)
    
    savings.deposit(2000)
    current.withdraw(3000)
    bank.transfer_balance(1,'S1001',2,'B1003',1500)
    
    Customer1.show_accounts()
    Customer2.show_accounts()
    