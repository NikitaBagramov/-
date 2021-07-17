def F(start,end):
    if end==34:
        return 0
    if end<start:
        return 0
    if start==end:
        return 1
    k=F(start,end-4)
    k+=F(start,end-11)
    if end%5==0:
        k+=F(start,end//5)
    return k
print(F(5,17)*F(17,112))#Ответ 3030
