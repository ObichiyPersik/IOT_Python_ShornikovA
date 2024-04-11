room = int(input())
num = 0
for i in range (1,5):
    for j in range (1,9):
        num+=1
        if(num) == room:
            print(j," ",i)
    j=0