t=[] #cu virgule
with open('input.txt','r')as f:
    for i in f:
        t.append([int(x) for x in i.split(',')])
print(t)
a,Sum,dp,ds=[],[],[],[]
for i in t:
    a.append(sum(i))
for j in range(len(t)):
    s=0
    for k in range(len(t[0])-1,-1,-1):
        s=s+t[k][j]
        if(k==j):
            dp.append(t[j][k])
        if(k+j==len(t)-1):
           ds.append(t[j][k])
    Sum.append(s)
with open('output.txt','w')as f:
    f.write("{1}{0}{2}{0}{3}{0}{4}".format('\n',str(a),str(Sum),str(dp),str(ds)))