def F(start,end):
    if end <start:
        return 0
    if start==end:
        return 1
    k=F(start,end-2)
    k+=F(start,end-5)
    if end%3==0:
        k+=F(start,end//3)
    return k
print(F(2,34))#Ответ 493
