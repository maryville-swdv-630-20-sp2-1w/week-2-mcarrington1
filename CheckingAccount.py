class CheckingAccount:
    """
    This class is a model of a bank account. This includes a transactions dict to keep track of transactions by a given ID
    """
    def __init__(self, accountNumber, firstName, lastName, address, balance=0.00):
        self.accountNumber = accountNumber
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self._balance = balance
        self.transactions = {}
    
    def creditAccount(self, transactionId, creditAmount):
        self.transactions[transactionId] = creditAmount
        self._balance += creditAmount
        print('Account credited:{:8.2f}. Balance is:{:8.2f}'.format(creditAmount, self._balance))
    
    def debitAccount(self, transactionId, debitAmount):
        if debitAmount + self._balance < 0:
            raise ValueError("Insufficient Funds...")
        else:
            self.transactions[transactionId] = debitAmount
            self._balance += debitAmount
            print('Account debited:{:8.2f}. Balance is:{:8.2f}'.format(debitAmount, self._balance))

    def updateAddress(self, address):
        self.address = address
        
    def getBalance(self):
        return self._balance
    
    def getTransactionAmountById(self, transactionId):
        return self.transactions.get(transactionId, "No Transaction Found")
        
    def getAllTransactions(self):
        return self.transactions
        

def main():
    account = CheckingAccount('8675309','Matt','Carrington','22 San Camille court. 63303', 15.55)
    print('Account Name is: {} {}'.format(account.firstName, account.lastName))
    print('Account Balance is: {}'.format(account.getBalance()))
    account.creditAccount('123456789', 5.00)
    account.creditAccount('123456790', 155.00)
    account.debitAccount('123456791', -20.55)
    print('Transactions (Single): {}'.format(account.getTransactionAmountById('123456789')))
    print('Transactions (ALL): {}'.format(account.getAllTransactions()))
    
main()