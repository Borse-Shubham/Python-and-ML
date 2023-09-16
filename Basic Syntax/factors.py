
def DisplayFactors(value):
    for i in range(1,value,1):
        if(value % i == 0):
            print(i)


def main():        
    no = 0
    print("Enter number")
    no = int(input())
    DisplayFactors(no)

if __name__=="__main__":
    main()