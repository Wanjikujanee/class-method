from datetime import datetime
from re import X

class Account():
    def __init__(self,account_name,acc_number):
        self.account_name=account_name
        self.acc_number=acc_number
        self.balance=0
        self.deposits=[]
        self.withdraws=[]
        self.transaction=100
        self.time=datetime.now()
        self.loan_balance=0




    def deposit(self,amount):
        if amount<=0:


            return f"Deposit amount should be more than zero"
        else:
            self.balance+=amount
            self.deposits.append(amount)

            self.deposits.append({"date":self.time.strftime("%c"),"amount":amount,"narration":"deposit"})
            return  self.balance   


    def withdraw(self,amount):
        self.transaction=100
        if amount<=0: 
         return f"withdraw should be greater than zero"   

        elif amount + self.transaction >self.balance:  
            return f"your balance {self.balance} you cant withdraw amount"

        else:
            self.balance-=amount+self.transaction
            self.withdraws.append(amount)
            self.withdraws.append({"date":self.time.strftime("%c"),"amount":amount,"narration":"withdraw"})
            return f"hello {self.account_name} you have withdraw {amount} your new balance is {self.balance}"
 ##Add a new method called deposits_statement 
 # which using a for loop prints
    def  deposits_statement (self):
     print(X,end="\n")
#Add a new method called withdrawals_statement which using
#  a for loop prints each withdrawal in a new line
    def  wwithdraws_statement (self):
     def  withdraws_statement (self):
        for x in self.withdraws:
            print(x,end="\n")
            print(x,"\n")

            #Add a method to show the current balance.
    def current_balance(self):
        return f"{self.balance}"


    def full_statement(self):
              for money_transaction in self.statement:
                  amount=money_transaction["amount"]
                  Narration=money_transaction["Narration"]
                  time=money_transaction["time"]
                  date=time.strftime("%x/%X")
                  print(f"{date}: {Narration} {amount}")



      #Add a borrow method which allows a customer to borrow if they meet these conditions:
# Customer has made at least 10 deposits.
# Loan amount requested must be more than 100
# A customer qualifies for a loan amount that is less than  or equal 
# to 1/3 of their total sum of deposit history
# Customer account has no has no balance
# Customer has no outstanding loan
# The loan attracts  an interest of 3%.       

    def  borrow_loans(self,loan_amount):
            self.loan_amount=loan_amount
            self.interest=0.03*self.loan_amount
            self.total_loan=self.loan_amount+self.interest
            if len(self.deposits)>10 and loan_amount<=sum(self.deposits)//3 and loan_amount>100 and self.balance<0:
                print(f"You have been awarded a loan of {loan_amount} your current balance is {self.amount}")
            else:
                print("You are not eligible for a loan")


    def transfer(self,receiver,amount):
            self.receiver=receiver
            self.amount=amount
            current_balance=self.balance-amount
            if amount<=0:
                print( f"You cannot transfer a non-existant amount")
            elif amount>self.balance:
                print(f"Your cannot transfer {amount}.Your current balance is {self.balance}")
            else :
                amount<self.balance
                print(f"You have transfered {amount} to {self.receiver} your current balance is {current_balance}")
    def  borrow_loans(self,loan_amount):
            self.loan_amount=loan_amount
            self.interest=0.03*self.loan_amount
            self.total_loan=self.loan_amount+self.interest
            if len(self.deposits)>10 and loan_amount<=sum(self.deposits)//3 and loan_amount>100 and self.balance<0:
                print(f"You have been awarded a loan of {loan_amount} your current balance is {self.amount}")
            else:
                print("sorry {self.acc}you are not eligible for a loan")
    def pay_loans(self,amount_payloan):
              self.amount_payloan=amount_payloan
              self.interest=0.03*self.loan_amount
              total_topay=amount_payloan+self.interest
              loan_remaining=self.loan_amount-amount_payloan
              new_balance=self.loan_amount-total_topay
              if total_topay>0:
                  print(f"You have deposited {amount_payloan} your loan of {self.loan_amount}Ksh.Your new loan balance is {new_balance}Ksh")
              elif total_topay>loan_remaining:
                  print(f"Congratulations!! You have cleared your loan of {self.amount}.Your new balance is{new_balance}")
              else:
                  print(f"You have a loan balance of {self.total_loan}")
    def current_balance(self):
             print(f"Your current balance {self.balance}Ksh" )