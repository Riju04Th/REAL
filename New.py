n = int(input("Enter rows of space: "))
k = int(input("enter the Number on rows: "))
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()
