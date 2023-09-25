import functools

    
def main():
    Data = []
    print("Enter number of elements : ")
    Size = int(input())
    
    print("Enter the elements :")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Input data : ",Data)

    output = list(filter((lambda No : (No%2==0)),Data))
    print("Result after filter : " ,output)

    moutput = list(map(lambda No :  No + 2,output))
    print("Result after add : ",moutput)

    result = functools.reduce((lambda No1 , No2 : No1 + No2),moutput)
    print("Result after reduce : ",result)

if __name__=="__main__":
    main()