ll= ['2017001', '2016001', '2017002', '2017009', '2016100', '2016210', '1995091', '1996002', '1999010', '2003100', '2007301']

#type 1

l1=[i for i in l if 1995<= int(i[:4]) <=2005]
print(l1)
print(len(l1))
##for i in l:
##    print(i[4:])


#type 2

from collections import defaultdict
d=defaultdict(list)
for i in l:
    d[i[:4]].append(i)
for k,v in d.items():
    if k in range (1995,2006):
        print(k,'=',len(v))


