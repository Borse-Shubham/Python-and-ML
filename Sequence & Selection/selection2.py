def CheckEven(value):
    result = value % 2

    if(result == 0):
        print("number is even")
    else:
        print("number is odd")

def main():
    no = 0

    print("Enter number : ")
    no = int(input())

    CheckEven(no)


if __name__ == "__main__":
    main()