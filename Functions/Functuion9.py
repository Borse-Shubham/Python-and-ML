def Add(A,B):
    return A + B

def Marvellous(FPTR1):
    print(type(FPTR1))
    print(FPTR1)
    Ans = FPTR1(11,7)
    print("Addition is : ",Ans)


def main():
    Marvellous(Add)


if __name__=="__main__":
    main()