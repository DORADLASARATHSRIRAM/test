def count(x,y):
    last=y[len(y)-1]
    res=0
    for i in x:
        if i==last:
            res+=1
    return res
x=input()
y=input()
print(count(x,y))
