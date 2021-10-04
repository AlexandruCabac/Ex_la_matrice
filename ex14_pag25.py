t,udp,bdp,dp,uds,bds,ds=[],[],[],[],[],[],[]
with open('input.txt','r')as f:
    n=int(f.readline())
    for i in f:
        t.append([int(x) for x in i.split(',')])
if(int(n)>=2 and int(n)<=10):
    for j in range(len(t)):
        for k in range(len(t[0])-1,-1,-1):
            if(k==j):
                dp.append(t[j][k])
            if(k+j==len(t)-1):
                ds.append(t[j][k])
            if(k<j):
                bdp.append(t[j][k])
            if(k>j):
                udp.append(t[j][k])
            if(j+k<len(t)-1):
                uds.append(t[j][k])
            if(j+k>len(t)-1):
                bds.append(t[j][k])
with open('output.txt','w')as f:
    f.write("{1}{0}{2}{0}{3}{0}{4}{0}{5}{0}{6}".format('\n',str(sum(dp)),str(sum(ds)),str(sum(udp)),str(sum(bdp)),str(sum(uds)),str(sum(bds))))