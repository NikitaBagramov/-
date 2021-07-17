def F(start,end):
    if start==136:
        return 0
    if start>end:
        return 0
    if start==end:
        return 1
    k=F(start+11,end)
    k+=F(start+32,end)
    k+=F(start**3,end)
    return k
print(F(4,59)*F(59,211))#42
