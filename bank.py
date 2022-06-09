class Account:
      def __init__(self,name,acc_number,):
                 self.balance = 0
                 self.name = name
                 self.acc_number=acc_number
                 self.deposits=[]
                 self.withdrawal=[]
                 
                 
                 
              

      def deposit(self,amount):
             if amount<=0:
                    return f"Deposit amount should be more than zero"
             self.balance+=amount
             self.deposit.append(amount)
             return f"You have deposited {amount} .Your new balance is {self.balance}",self.deposit
      
                 
      def deposit_statement(self):
                    print(*self.deposit,sep="/n")
      
      def withdraw(self,amount):
             if amount>self.balance:
                    return f"Your balance is {self.balance} .You cannot withdraw the {amount}"
             elif amount<=0:
                    return f"Amount must e greater than zero"
             else:
                    self.balance==amount
                    self.withdraw.append(amount)
                    return f"You have withdrawn {amount}  your balance is {self.balance}",self.withdraw
             
      def withdraw_statement(self):
                    print(*self.withdraw,sep="/n")
             
             
             
             
             
           