from functools import reduce

CheckEven = lambda No : (No%2==0)


Increase = lambda No :  No + 2

Add = lambda No1 , No2 : No1 + No2

def main():
    Data = []
    print("Enter number of elements : ")
    Size = int(input())
    
    print("Enter the elements :")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Input data : ",Data)

    output = list(filter(CheckEven,Data))
    print(output)

    moutput = list(map(Increase,output))
    print(moutput)

    result = reduce(Add,moutput)
    print(result)

if __name__=="__main__":
    main()