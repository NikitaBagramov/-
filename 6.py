def even(x):
    if x%2==0:
        return x
    else:
        return x+1
def difference(x):
    ma=[]
    su=0
    dif=x%3
    while x>0:
        ma.append(x%7)
        x//=7
    ma[0]=abs(ma[0]-dif)
    for i in range(len(ma)):
        su+=ma[i]*(7**i)
    return su
mas=set()
def F(value,step):
    if step>10:
        return 0
    if step==10:
        mas.add(value)
    F(int(value**1.5),step+1)
    F(even(value),step+1)
    F(value+6,step+1)
    F(difference(value),step+1)
F(222,0)
print(len(mas))#Ответ 12549
