Set1 = {11,78.89,"hellow",True}
print(Set1)

#print(Set1[1])

for i in Set1:
    print(i)

Set2 = {11,78,89,11,78}
print(Set2)

Set2.add(101)
print(Set2)
Set2.remove(101)
print(Set2)

print("Enter the value that you want to search in set ")
N=(int(input()))
for value in Set2:
    if(N == value ):
        print("yes")