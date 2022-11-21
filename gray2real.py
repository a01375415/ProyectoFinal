def gray2real(indiv):
    g0=indiv[0:6]
    g1=indiv[6:12]
    g2=indiv[12:18]
    g3=indiv[18:24]
    b0=[g0[0]]
    b1=[g1[0]]
    b2=[g2[0]]
    b3=[g3[0]]
    
    for i in range(5):
        b0.append(int(b0[i])^int(g0[i+1]))
        b1.append(int(b1[i])^int(g1[i+1]))
        b2.append(int(b2[i])^int(g2[i+1]))
        b3.append(int(b3[i])^int(g3[i+1]))
    r0=0
    r1=0
    r2=0
    r3=0   

    for i in range(len(b0)):
        r0+=b0[i]*2**(5-i)
        r1+=b1[i]*2**(5-i)
        r2+=b2[i]*2**(5-i)
        r3+=b3[i]*2**(5-i)    
    
    r0=r0+2
    r1=r1+2
    r2=r2+2
    r3=r3+2
    
    R=[r0,r1,r2,r3]

    return R