
def Addition(no1,no2):
    Result = 0
    Result = no1 + no2
    return Result

def main():
    value1= int(input("Enter First Number"))

    value2= int(input("Enter Second Number"))

    Answer = 0
    Answer = Addition(value1,value2)

    print("Addition is :",Answer)

main()