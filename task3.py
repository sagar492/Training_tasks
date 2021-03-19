data = '''Python is a wonderful language, it is easy to learn, it can handle large data easily, 
        it can handle strings and numbers and floats, and data in different file formats, I am eager to learn Python'''

#type 1

data1=data.split()
d={}
for i in data1:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

#type 2

from collections import defaultdict
d=defaultdict(list)
for i in data.split():
    if i in d:
        d[i]+=1
    else:
        d[i]=1
