def fourth(x):
    ma=[]
    while x>0:
        ma.append(x%2)
        x//=2
    ma[0]=0
    x1=0
    for i in range(len(ma)):
        x1+=ma[i]*(2**i)
    return x1
mas=set()
def F(value,step):
    if step>7:
        return 0
    if step==7:
        mas.add(value)
    F(value+15,step+1)
    F(value*4-value*4%7,step+1)
    F((value*3)//2,step+1)
    F(fourth(value),step+1)
F(17,0)
print(len(mas))#Ответ 1764
