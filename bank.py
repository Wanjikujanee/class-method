from curses import def_prog_mode


class Account:
      def __init__(self,name,balance,number,deposit,withdraw):
                 self.name = name
                 self.balance = balance
                 self.deposit = deposit
                 self.number = number
                 self.withdraw = withdraw
                
              

      def deposit(self,deposit):
             self.deposit=int(input("You  have deposited:"))
             self.balance+=self.deposit
             return f"Your new deposit  is {self.deposit}"


      def withdraw(self,withdraw):
        self.withdraw= int(input("You  have withdrawn:")) 
      if balance>=withdraw:
            balance-withdraw
            print("You have withdrawn:" ,withdraw)
      else:
             print("You have insufficient funds")
      def balance(self):
         print("Your current balance is :" , self.balance)
