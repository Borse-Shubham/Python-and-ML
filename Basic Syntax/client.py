import moduleintro

def main():
    value1 = int(input("Enter first number :"))
    value2 = int(input("Enter second number :"))

    result=0

    Result= moduleintro.Addition(value1,value2)
    print("Addition is : ",Result)


    Result= moduleintro.Substraction(value1,value2)
    print("substraction is  : ",Result)


    Result= moduleintro.Multiplication(value1,value2)
    print("multiplication is : ",Result)

if __name__=="__main__":
    main()