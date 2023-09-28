#fuction returns nothing and accept more parameter

def Marvellous(Name,Age,City):
    print("Inside Marvellous Function")
    print("Welcome :",Name)
    print("Your Age is : ",Age)
    print("Your City is : ",City)

def main():
   Marvellous("Amit",28,"pune") 
   Marvellous(City = "Mumbai" , Age = 30 , Name = "Sagar")
 


if __name__=="__main__":
    main()