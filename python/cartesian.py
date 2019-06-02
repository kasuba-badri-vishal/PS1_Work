def swap(a,b):
    temp = a
    a = b
    b = temp

a = list(map(int,input().split()))
b = list(map(int,input().split()))

for i in range(0,len(a)-1):
    for j in range(1,len(a)):
        if(a[i]>a[j]):
            swap(a[i],a[j])

for i in range(0,len(b)-1):
    for j in range(1,len(b)):
        if(b[i]>b[j]):
            swap(b[i],b[j])
for i in a:
    for j in b:
        print("(",end="")
        print(i,end="")
        print(",",end=" ")
        print(j,end="")
        print(")",end=" ")