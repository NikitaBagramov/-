def two_to_ten(ma):
    ma.reverse()
    su=0
    for i in range(len(ma)):
        su+=ma[i]*(2**i)
    return su
def inversion(x):
    ma_rev=[]
    while x>0:
        ma_rev.append(x%2)
        x//=2
    ma_rev.reverse()
    if ma_rev[0]==0:
        ma_rev[0]=1
    else:
        ma_rev[0]=0
    return two_to_ten(ma_rev)
def shift(x):
    ma=[]
    while x>0:
        ma.append(x%2)
        x//=2
    ma.reverse()
    ma.append(ma[0])
    ma[0]=0
    return two_to_ten(ma)
def binary_account(x):
    ma=[]
    while x>0:
        ma.append(x%2)
        x//=2
    ma.reverse()
    ma.append(sum(ma)%2)
    return two_to_ten(ma)
answer=[]
def F(value,step):
    if step>6:
        return 0
    if value==0:
        return 0
    if step==6:
        answer.append(value)
    F(shift(value),step+1)
    F(binary_account(value),step+1)
    F(inversion(value),step+1)
    if value%7<4:
        F(value+4,step+1)
    F(int(value),step+1)
F(42,0)
answer.sort(reverse=True)
for x in answer:
    if int(x**0.5)**2==x:
        print(x)
        break
