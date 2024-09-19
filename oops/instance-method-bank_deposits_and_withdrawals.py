#A class to handle bank deposits and withdrawals
import sys
class Bank(object):
    def __init__(self,name,balance=0.0) -> None:
        self.name=name
        self.balance=balance
        pass
    #to add deposit amount to balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
        
    #to deduct withdrawal amount from balance 
    def withdraw(self,amount):
        if amount>self.balance:
            print('you do not have sufficient balance for withdrawal')
        else:
            self.balance-=amount
            return self.balance
        
            
# create an account with the given name and balance 0.0
name=input('Enter your Name: ')
b=Bank(name)  #this is instance of bank account
while(True):
    print('d-deposit,w-withdrawal,e-exit')
    choice=input('Your Choice: ')
    if choice=='e' or choice=='E':
        exit()
    elif choice.isdigit():
        print('Kindly Enter your correct choice---')
        continue
        
    amt=float(input('Enter the amount: '))
    
    #Transaction
    if choice=='d' or choice=='D':
        print('Balance after deposit:',b.deposit(amt))
    elif choice=='w' or choice=='W':
        print('Balance after withdrawal:',b.withdraw(amt))