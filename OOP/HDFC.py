class HDFC():
    ROI = 9.5

    def __init__(self,Name,Amount):
        self.AccountHolder = Name
        self.Balance = Amount
        print("Welcome ",self.AccountHolder)
        print("Account gets succesfully created with initial balance : ",self.Balance)

    def DisplayBalance(self):
        print("Hello",self.AccountHolder)
        print("Your account balance is : ", self.Balance)

    @classmethod
    def DisplayBankInfo(cls):
        print("Welcome to HDFC bank portal")
        print("Our bank is pvt")
        print("We provide the rate of intrest on saving account is : ",cls.ROI)

    @staticmethod
    def DisplayKYCInfo():
        print("According to the rules of RBI you should probide below documents  for KYC")
        print("your Adhar card")
        print("your PAN card")
        print("your paasport size photo ")

    def Withdraw(self,Amount):
        if self.Balance < Amount:
            print("There is no sufficient balance ")

        else:
            self.Balance = self.Balance-Amount 
            print("Amount withdrawal succesful...")

    def Deposite(self ,Amount):
        self.Balance = self.Balance + Amount
        print("Amount deposited succesful...")

def main():
    print("ROI of HDFC bank is : ",HDFC.ROI )

    HDFC.DisplayBankInfo()

    HDFC.DisplayKYCInfo()

    print("Creating new Account...")
    obj1 = HDFC("Amit",5000)

    print("Creating new Account...")
    obj2 = HDFC("Sagar",3000)

    print("Performing operations on OBJ1")
    obj1.Deposite(2000)
    obj1.DisplayBalance()

    obj1.Withdraw(1000)
    obj1.DisplayBalance()

    print("Performing operations on Sagar's Acount")
    obj2.Deposite(4000)
    obj2.DisplayBalance()

    obj2.Withdraw(500)
    obj2.DisplayBalance()


if __name__=="__main__":
     main()
