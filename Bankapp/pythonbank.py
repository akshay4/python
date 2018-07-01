print("#############################################################################")
print ("Welcome to Python Bank")                                    
prompt=int(input("""To open a new Bank Account, Press 1\n"""+"""To access your Existing Account or to Transact press 2\n"""))    
if prompt==1:
    cus=BankAccount()                                
elif prompt==2:
    cus=ReturnCustomer()                            
else:
    print ("You have pressed the wrong key, please try again")                                                                                             
print("#############################################################################")

class BankAccount:
    """Class for a bank account"""
    def __init__(self):
        self.username = cusaccountcheck()
        self.userpassword = cusaccountcheck()
        self.balance = cusaccountcheck()
        print ("Thank you %s, your account is set up and ready to use,\n a intial amout has been credited to your account" %self.username)
        time.sleep(2)
        self.userfunctions()

    def useraccount(self):
        print("\n\nTo access any function below, enter the corresponding key")
        print("""To:Check Balance, press B\n
        Deposit Cash,  press D\n
        Withdraw Cash, press W\n
        Delete Account press Xln
        Exit Service,  press E\n:"""),
        ans=input("").lower()
        if ans=='b':
            self.passcheck()
            self.checkbalance()
        elif ans=='d':
            self.passcheck()
            self.depositcash()
        elif ans=='w':
            self.passcheck()
            self.withdrawcash()
        elif ans=='x':
            print ("%s, your Account is being Deleted"%self.username)
            time.sleep(1)
            print ("Work in Progress")
            time.sleep(1)
            filestore.deleteaccount(self.username)
            print ("Your Account has been successfuly Deleted, thankyou for having you with Us.")
        elif ans=='e':
            print ("Thank you for using Python Bank Services")
            time.sleep(1)
            print ("Goodbye %s" %self.username)
            exit()
        else:
            print ("Input Error, please try again")
            self.userfunctions()

    def checkbalance(self):
        date=datetime.date.today()
        date=date.strftime('%d-%B-%Y')
        self.working()
        print ("Your account balance as at {} is {}".format(date, self.balance))
        self.transact_again()

    def withdrawcash(self):
        amount=float(input("::\n Please enter amount to withdraw\n: "))
        self.balance-=amount
        self.working()
        print ("Your new account balance is %.2f" %self.balance)
        print ("::\n")
        filestore.balupdate(self.username, -amount)
        self.transact_again()

    def depositcash(self):
        amount=float(input("::\nPlease enter amount to be deposited\n: "))
        self.balance+=amount
        self.working()
        print ("Your new account balance is %.2f" %self.balance)
        print ("::\n")
        filestore.balupdate(self.username, amount)
        self.transact_again()

    def transact_again(self):
        ans=input("Do you want to do any other transaction? (y/n)\n").lower()
        self.working()
        if ans=='y':
            self.userfunctions()
        elif ans=='n':
            print ("Thank you for using Python Bank. Have a good day")
            time.sleep(1)
            print ("Goodbye {}").format(self.username)
            exit()
        elif ans!='y' and ans!='n':
            print("Unknown key pressed, please choose either 'N' or 'Y'")
            self.transact_again()

    def working(self):
        print("working"),
        time.sleep(1)
        print ("..")
        time.sleep(1)
        print("..")
        time.sleep(1)


    def passcheck(self):
        """prompts user for password with every transaction and counterchecks it with stored passwords"""
        b=3
        while b>0:
            ans=input("Please type in your password to continue with the transaction\n: ")
            if ans==self.userpassword:
                return True
            else:
                print("That is the wrong password")
                b-=1
                print ("%d more attempt(s) remaining" %b)

        print ("Account has been freezed due to three wrong password attempts,\n contact your bank for help, bye bye")
        time.sleep(1)
        print ("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        exit()

class ReturnCustomer(BankAccount):
    def __init__(self):
        self.username, self.userpassword, self.balance=filestore.oldcuscheck()
        self.userfunctions()
        
        
    
        
    def cusaccountcheck():
        """creates a new user if it does not exist"""
        name=""
        pin=""

        while name not in cusnames and len(name)<3 :
                name=input("Please type in your name for this new bank account\n")
                if name not in cusnames:
                        cusnames.append(name)
                        filewrite(cusnames)
                        break
                print("Sorry, that user name is already in use")
                ans=input("Are you already a member at this bank? (y/n)\n")
                if ans.lower()=='y':
                        oldcuscheck()
                else:
                        cusaccountcheck()

        while len(pin)<4:
                pin=raw_input("Please assign a password to this account, pin should be at least 5 characters\n")
                if len(pin)>4:
                        print("your pin has been successfully saved")
                        print("Remember to always keep your pin safe and don't disclose it to anybody")
                        cuspasswords.append(pin)
                        cusbalance.append(0)
                        balance=100.0
                        cusbalance[cusnames.index(name)]=balance
                        filewrite(cuspasswords)
                        filewrite(cusbalance)
                        break
                print ("Sorry, that is a short password")
        return name,pin, balance
    
    def oldcuscheck():
        """checking returning customer"""
        name=""
        while name not in cusnames:
                name=input("What is your name?\n")
                if name in cusnames:
                        username=name
                        userpassword=cuspasswords[cusnames.index(name)]
                        balance=float(cusbalance[cusnames.index(name)])
                        return username, userpassword, balance
                else:
                        print ("Sorry %s, It looks like you didn't spell you name correctly or your name is not in our records"%name)
                        again=input("would like to type in your name again? (y/n)")
                        if again.lower()=='y':
                                oldcuscheck()
                        else:
                                print ("Bye bye, thank you for trying Postbank")
                                exit()

    def filewrite(item):
        """defination to write data into files."""
        if item==cusnames:
                text=open("cusnamefile.txt","w")
                for i in item:
                        text.write(i+"\n")
                text.close()

        elif item==cuspasswords:
                text=open("cuspassfile.txt", "w")
                for i in item:
                        text.write(i+"\n")
                text.close()

        elif item==cusbalance:
                text=open("cusbalfile.txt", "w")
                for i in item:
                        text.write(str(i)+"\n")
                text.close()
                
    def balupdate(ind, amount):
        ccountnumber=cusnames.index(ind)
        accountbal=float(cusbalance[accountnumber])
        accountbal+=amount
        cusbalance[accountnumber]=accountbal
        text=open("cusbalfile.txt", "w")
        for i in cusbalance:
                text.write(str(i)+"\n")
        text.close()
    def deleteaccount(name):
        accountnumber=cusnames.index(name)
        del cusnames[accountnumber]
        filewrite(cusnames)
        del cusbalance[accountnumber]
        filewrite(cusbalance)
        del cuspasswords[accountnumber]
        filewrite(cuspasswords)
        return None  