def F(start,end):
    if start>end:
        return 0
    if start==end:
        return 1
    k=F(start+3,end)
    k+=F(start+7,end)
    k+=F(start**2,end)
    return k
print(F(13,92)) #Ответ:25744
