aux=0
for o in range(0,m):
    temp=1
    k=o
    for i in range(0, m):
        temp=temp * M1[i][k]
        k+1=1
        if(k==m):
            k=0
    aux+=temp
for o in range(m-1,-1,-1):
    temp=1
    k=0
    for i in range(0,n):
        temp=temp * M1[i][k]
        k-=1
        if(k==-1):
            aux-=temp
print("Determinante:",aux)

