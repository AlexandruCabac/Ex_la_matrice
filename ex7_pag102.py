t=[['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001'],
    ['0000','0001','0011','0010','0110','0111','0101','0100','1100','1101'],
    ['0000','0001','0010','0011','0100','1011','1100','1101','1110','1111'],
    ['0011','0100','0101','0110','0111','1000','1001','1010','1011','1100']]
a,s=[],''
with open('input.txt','r')as f:
    n1=f.readline()
    n2=f.readline()
if(n2=='Direct'):
    a=t[0]
if(n2=='Gray'):
    a=t[1]
if(n2=='Aiken'):
    a=t[2]
if(n2=='Exces 3'):
    a=t[3]
if(len(a)!=0):
    for i in range(0,len(n1)-1):
        s=s+str(a[int(n1[i])])+', '
with open('output.txt','w')as f:
    f.write(s[:len(s)-2])