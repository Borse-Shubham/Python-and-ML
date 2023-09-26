def Display(*values):
    for i in range(len(values)):
        print(values[i])
    

def main():
    print("demonstration of positional arguments")

    Display(10,20,30,40,50,60)
    Display(11,21,51)

if __name__=="__main__":
    main()