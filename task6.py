#NameError
try:
    a=10
    b=20
    if a > c:
        print(a)
    else:
        print(c)
except NameError:
    print('name not found')
finally:
    print('printing finally')


# ioError

try:
    with open('data.txt') as f:
        for line in f:
            print(line)
except IOError:
    print('file not found')
