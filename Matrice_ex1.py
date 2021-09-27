a=[[1,2,3,4,5],[15,-25,35,-45,55],[-1,-2,-3,-4,-5],[32,51,23,47,3],[92,61,30,52,10]]
dp,ds=[],[]
for i in a:
    print(sum(i))
for j in range(len(a)):
    s=0
    for k in range(len(a[0])-1,-1,-1):
        s=s+a[k][j]
        if(k==j):
            dp.append(a[j][k])
        if(k+j==len(a)-1):
           ds.append(a[j][k])
    print(s)
print(dp,ds)