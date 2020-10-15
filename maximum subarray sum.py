a=list()

a=[4,5,6,1,2,6]
msum=0
for i in range(0,len(a)):
    for j in range(i,len(a)):
        sum1=0
        for k in range(i,j+1):
            sum1=sum1+a[k]

        if sum1>msum:
            msum=sum1

print(msum)
