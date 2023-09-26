def Display(Name, Age, Marks):
    print("Name is : ",Name)
    print("Age is : ",Age)
    print("Marks are : ", Marks)

def main():
    print("demonstration of positional arguments")

    Display("Amit",Age=25,Marks=89)

    Display(Marks=78,Name="Sagar",Age=28)

if __name__=="__main__":
    main()