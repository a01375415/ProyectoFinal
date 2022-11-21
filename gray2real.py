def convreal(indiv):
    n=len(indiv)-1
    b=[indiv[0]]
    for i in range(n):
        b.append(int(b[i])^int(indiv[i+1]))
    r=0
    for i in range(n+1):
        r+=b[i]*2**(n-i)
    return r

def gray2real(indiv):
    g0=indiv[0:10]
    g1=indiv[10:14]
    g2=indiv[14:19]
    g3=indiv[19:24]
    r0=convreal(g0)+2
    r1=convreal(g1)+2
    r2=convreal(g2)+1
    r3=convreal(g3)+1
        
    R=[r0,r1,r2,r3]

    return R