def Display(*values):
    print(type(values))
    print(len(values))
    print(values)
    

def main():
    print("demonstration of positional arguments")

    Display(10,20,30,40,50,60)

if __name__=="__main__":
    main()