import time
print("Welcome to MY ATM")
print("Swipe Card")
amount=1000000

o="4078"
print("_________________")
p=input("enter pin")
print("Verifying.......!!")
time.sleep(3)
if p==o:
  print("1.Cash Withdrawl")
  print("2.Check enquiry")
  print("3.Balance enquiry")
  print("4.Print receipt")
  print("5.Mini Statement")
  print("6.Exit")

  ch=int(input("enter your choice"))
  if ch==1:
     print("c.Current")
     print("s.Savings")
     print("________________")
     h=input("enter your option")
     if h=='c':
        wdraw=input("enter the amount to be withdraw:")
        print("Transaction Done")
        print("Take Amount")
        print("Hope you had nice time")
     else:
        sdraw=input("enter the amount to withdraw:")
        print("Transaction Successful")
        print("Take amount")
        print("Hope you had nice time")
  elif ch==2:
     print(f"Current Balance is {amount}")
     print("Hope you had nice time")
  elif ch==3:
     print(f"Balance is {amount}")
     print("Hope you had nice time")
  elif ch==4:
     yn=input("Print Receipt.{amount} yes/no")
     if yn=='yes':
         print("Take Receipt")
     elif yn=='no':
         print("Hope you had nice time")
     else:
         print("error 404")          
  elif ch==5:
     print("Take your mini statement of balance")
     print("Hope you had nice time")

  elif ch==6:
     exit()             
     


  else:
      print("error")
                   
else:
  print("Invalid Pin ,Try again")
  
  
