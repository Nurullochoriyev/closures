def fibanachi(n):
    a=0
    b=1
    # c=0
    for i in range(2,n):
        c=a+b
        a=b
        b=c

    return b
# fibanachi(7)
print(fibanachi(10))