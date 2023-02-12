  
from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017")
import datetime
import time
import random
import re
print("****BANKING****")
print("Welcome to the bank of caesar \n #India's No:1 bank")
class atm:
    def __init__(self):
        self.amt=0
        self.amt1=0
        self.account_number=0
        self.amount=0
        self.password=0
        self.pin=0
        self.phn=0
        self.amt1=0
        self.email=0
    def change_pin(self):
        print("----Change pin number---")
        for i in range(1,5):
            crpin=str(input("Enter your current pin number:"))
            if(crpin!=self.pin):
                print("please,Enter the correct pin")
            elif(crpin==self.pin):
                pass
                old_pin=crpin
                for i in range(1,5):
                    pin=str(input("Enter the new pin:"))
                    ps=len(pin)
                    if(ps<4):
                        print("please,enter the valid ")
                    elif(ps==4): 
                        pass
                        for i in range(1,5):
                            newpin=str(input("Re-Enter the pin number:"))
                            if(newpin!=pin):
                                print("Enter the matching valid pin number")
                            elif(newpin==pin):
                                pass
                                print("OPT number has been send to your register mobile number--->",self.phn)
                                for i in range(1,5):
                                    otp=random.randint(11111,99999)
                                    print(f"OTP==>{otp}")
                                    otp1=int(input("please,enter the otp:"))
                                    if(otp1!=otp):
                                        print("please,enter the correct otp")
                                    else:
                                        pass
                                        print("Your pin number has been updated successfully")
                                        self.pin= newpin
                                        coll=client["bankdetails"]
                                        transactiondetails=str(self.account_number)
                                        collection=coll[transactiondetails]
                                        n1={"pin_number":old_pin}
                                        n2={"$set":{"pin_number":newpin}}
                                        collection.update_one(n1,n2)
                                        a=str(input("Did need to find your data Yes/No:"))                
                                        if(a=="yes"):
                                            for i in collection.find({}):
                                                print("*****pin Changed*****")
                                                print("Name:",i["Customer name"])
                                                print("Account no:",i["Account no"])
                                                print("updated pin:",i["pin_number"])
                                                return("Thanks for using bank of caeasar")
                                        elif(a=="no"):
                                            return("Your transaction has been done successfully\nThanks for using bank of caeasar")
                                    
                                
    def amount_deposit(self):
        print("-----Deposit Amount------")
        self.amt1=int(input("Enter the amount:"))
        for i in range(1,5):
            dpin=str(input("Enter the pin number:"))
            if(dpin!=self.pin):
                print("please,Enter the correct pin")
            else:
                pass
                bal=self.amt1+self.amount
                self.amount=bal
                print("Amount Deposited==>",self.amt1)
                print("Total balance==>",bal)
                a=datetime.date.today()
                b=str(a)
                c=time.ctime()
                d=str(c)
                coll=client["bankdetails"]
                transactiondetails=str(self.account_number)
                collection=coll[transactiondetails]
                collection.insert_one({"Date":b,"Time":d,"Amount Deposited":self.amt1,"Total Balance":self.amount})
                collection.update_one({},{"$set":{"Amount Deposited":self.amt1,"Total Balance":self.amount}})
                for i in range(0,1):
                    a=str(input("Did need to find your data Yes/No:"))                
                    if(a=="yes"):
                        for i in collection.find({}):
                            print("*****Amount Deposited*****")
                            print("Name:",i["Customer name"])
                            print("Amount deposited:",i["Amount Deposited"])
                            print("Total Balance:",i["Total Balance"])
                            return("Your transaction has been done successfully")                
                    elif(a=="no"):
                        return("Your transaction has been done successfully\nThanks for using bank of caeasar")
    def amount_withdraw(self):
        print("-------withdraw amount--------")
        for i in range(1,5):
            self.amt=int(input("Enter the amount:"))
            if(self.amt>self.amount):
                print(f"Please,Enter the less than{self.amount}")
            else:
                pass
                for i in range(1,5):
                    wpin=str(input("Enter the pin number:"))
                    if(wpin!=self.pin):
                        print("please,Enter the correct pin")
                    else:
                        pass            
                        damt=self.amount-self.amt
                        self.amount=damt
                        print(self.amt,"<==ruppes you have debited")
                        print(self.amount,"<==Total balance in your account")
                        a=datetime.date.today()
                        b=str(a)
                        c=time.ctime()
                        d=str(c)
                        coll=client["bankdetails"]
                        transactiondetails=str(self.account_number)
                        collection=coll[transactiondetails]
                        collection.insert_one({"Date":b,"Time":d,"Amount withdrawn":self.amt,"Total Balance": self.amount})
                        collection.update_one({},{"$set":{"Amount withdrawn":self.amt,"Total Balance": self.amount}})
                        for i in range(0,1):
                            a=str(input("Did need to view your data yes/no:"))                
                            if(a=="yes"):
                                for i in collection.find({}):
                                    print("Name:",i["Customer name"])
                                    print("Amount_withdrawn",i["Amount withdrawn"])
                                    print("Total Balance:",i["Total Balance"])
                                    return("Your transaction has been done successfully")
                            elif(a=="no"):
                                return("Your transaction has been done successfully\nThanks for using bank of caeasar")            
    def check_balance(self):
        print("----checking_balance----")
        for i in range(1,5):
            cpin=str(input("Enter the pin number:"))
            if(cpin!=self.pin):
                print("please,Enter the correct pin")
            else:
                pass
                print("Total Balance==>",self.amount)
                return("Thanks for using bank of caeasar")
    def statement(self):
        print("----bank Statement----")   
        print(f"Amount you have withdrawed ==>{self.amt}")
        print(f"Amount you have deposited ==>{self.amt1}")
        print(f"Total balance==>{self.amount}")
        return("Thank you for using bank of caesar")
    def createaccount(self):
        print("----Welcome to the bank of caesar----")
        name=str(input("Enter the customer name:"))
        for i in range(1,5):
            mobileno=input("Enter the mobile number:")
            r=re.fullmatch("[6-9][0-9]{9}",mobileno)
            if r==None:
                print("Please,Enter the valid phone number")
            else:
                pass
                self.phn=mobileno
                address=str(input("Enter the Address:"))
                for i in range(1,5):
                    email=input("Enter your email id:")
                    r=re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",email)
                    if(r==None):
                        print("Please,Enter the Correct e-mail")
                    else:
                        pass
                        self.email=email
                        print(f"Passcode has been send to your registered email id==>{self.email}")
                        ra=random.randint(111111,999999)
                        print(f"passcode===>{ra}")
                        passcode=int(input("Enter the passcode:"))
                        if(passcode!=ra):
                            print("please enter the valid code")
                        elif(passcode==ra):                 
                            for i in range(1,5):
                                password=str(input("create your password more than 5 character:"))
                                ps=len(password)
                                if(ps<=5):
                                    print("please,enter the valid password")
                                elif(ps>5):
                                    pass
                                    for i in range(1,5):
                                        password1=str(input("Re-Enter the password:"))
                                        if(password1!=password):
                                            print("please,enter the matching password")
                                        else:
                                            print("Your password has been updated successfully")
                                            self.password=password1
                                            print(f"Otp as been sent to your registed mobile number==>{self.phn}")
                                            for i in range(1,5):
                                                otp=random.randint(00000,99999)
                                                print(f"OTP==>{otp}")
                                                otp1=int(input("please,enter the otp:"))
                                                if(otp1!=otp):
                                                    print("please,enter the correct otp")
                                                else:
                                                    pass
                                                    accountno=random.randint(000000000000000,999999999999999)
                                                    self.account_number=str(accountno)
                                                    print("--------------------------------------------------------------")
                                                    print(f"your account number has been generated==>{accountno}")
                                                    print("--------------------------------------------------------------")
                                                    for i in range(1,5):
                                                        pin=str(input("Set your four digit pin number:"))
                                                        ps=len(pin)
                                                        if(ps<4):
                                                            print("please,enter the valid pin")
                                                        else:
                                                            pass
                                                            for i in range(1,3):
                                                                pin1=str(input("Re-Enter your pin:"))
                                                                if(pin1!=pin):
                                                                    print("please,enter the matching pin")
                                                                else:
                                                                    pass
                                                                    print("Your pin number has been updated successfully")
                                                                    self.pin=pin1
                                                                    coll=client["bankdetails"]
                                                                    transactiondetails=str(self.account_number)
                                                                    collection=coll[transactiondetails]
                                                                    collection.insert_one({"Account no":self.account_number,"Customer name":name,"Mobile_number":self.phn,"Emailid":self.email,"Password":self.password,"pin_number":self.pin,"Address":address})
                                                                    a=str(input("Did need to view your data:"))                
                                                                    if(a=="yes"):
                                                                        for i in collection.find({}):
                                                                            print("Name:",i["Customer name"])
                                                                            print("Account no:",i["Account no"])
                                                                            print("Mobile Number:",i["Mobile_number"])
                                                                            print("Email_id:",i["Emailid"])
                                                                            print("password:",i["Password"])
                                                                            print("pin_number:",i["pin_number"])
                                                                            print("Address:",i["Address"])
                                                                            print("1-Deposit \n 2-Withdraw \n 3-Check balance \n 4-Reset pin \n 5-Bank Statement ")
                                                                            for i in range(1,4):
                                                                                user=0
                                                                                print(" ")
                                                                                user=int(input("Enter the choice:"))
                                                                                print(" ")
                                                                                if(user>6):
                                                                                    print("please,Enter the correct choice")
                                                                                elif(user==1):
                                                                                    print(self.amount_deposit())
                                                                                elif(user==2):
                                                                                    print(self.amount_withdraw())
                                                                                elif(user==3):
                                                                                    print(self.check_balance())
                                                                                elif(user==4):
                                                                                    print(self.change_pin())
                                                                                elif(user==5):
                                                                                    print(self.statement())
                                                                                else:    
                                                                                    print("Thank you for using bank of caesar")                                               
                                                                                                        
                                                                    elif(a=="no"):                                
                                                                        print("1-Deposit \n 2-Withdraw \n 3-Check balance \n 4-Reset pin \n 5-Bank Statement ")
                                                                        for i in range(1,4):
                                                                            user=0
                                                                            print(" ")
                                                                            user=int(input("Enter the choice:"))
                                                                            print(" ")
                                                                            if(user>6):
                                                                                print("please,Enter the correct choice")
                                                                            else:
                                                                                pass
                                                                                if(user==1):
                                                                                    print(self.amount_deposit())
                                                                                elif(user==2):
                                                                                    print(self.amount_withdraw())
                                                                                elif(user==3):
                                                                                    print(self.check_balance())
                                                                                elif(user==4):
                                                                                    print(self.change_pin())
                                                                                elif(user==5):
                                                                                    print(self.statement())
                                                                        else:    
                                                                            print("Thank you for using bank of caesar")
    def transaction(self):
        coll=client["bankdetails"]
        transactiondetails=input("Enter your Account number:")
        collection=coll[transactiondetails]
        a=input("Did need to continue your banking Yes/no:")              
        if(a=="yes"):
            a=str(input("Enter which date did you need your transaction details \n Enter the date as =>YYYY-MM-DD:"))
            for i in collection.find({"Date":a}):
                print(i," ")
                return(" ")
    def existingaccount(self):
        coll=client["bankdetails"]
        transactiondetails=input("Enter your Account number:")
        collection=coll[transactiondetails]
        a=input("Did need to continue your banking Yes/no:")              
        if(a=="yes"):
            #accno=int(transactiondetails)
            for i in collection.find({}):
                print(" ")
                print("***The bank of caesar welcoming again :)")
                print("Name:",i["Customer name"])
                print("Account no:",i["Account no"])
                print("Mobile Number:",i["Mobile_number"])
                print("Email_id:",i["Emailid"])
                print("Total Balance:",i["Total Balance"])
                self.account_number=i["Account no"]
                self.email=i["Emailid"]
                self.phn=i["Mobile_number"]
                self.pin=i["pin_number"]
                self.amount=i["Total Balance"]
                print(" ")
                print("1-Deposit \n 2-Withdraw \n 3-Check balance \n 4-Reset pin \n 5-Bank Statement ")
                for i in range(1,4):
                    user=0
                    print(" ")
                    user=int(input("Enter the choice:"))
                    print(" ")
                    if(user>6):
                        print("please,Enter the correct choice")
                    else:
                        pass
                        if(user==1):
                            print(self.amount_deposit())
                        elif(user==2):
                            print(self.amount_withdraw())
                        elif(user==3):
                            print(self.check_balance())
                        elif(user==4):
                            print(self.change_pin())
                        elif(user==5):
                            print(self.statement())
                        else:    
                            print("Thank you for using bank of caesar")
                else:
                    print("Thank you for using bank of caesar")                   
        else:
            return("Thank you for using bank of caesar")            
class bank(atm):
    def final(self):
        print("1.Creating account \n 2.Existing using \n 3.View Entire Transaction ")
        for i in range(1,5):
            option=int(input("Enter the option:"))
            if(option>3):
                print("please,Enter the correct option")
            elif(option==1):
                print(p1.createaccount())
            elif(option==2):
                print(p1.existingaccount())
            elif(option==3):
                print(p1.transaction())
        else:
            print("Thank you for using bank of caesar")
        
p1=bank()
p1.final()

