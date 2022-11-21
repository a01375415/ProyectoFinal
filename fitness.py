#Resistor voltage measured/simulated data
VR_data = [1.00E-07, 2.50E-02, 1.00E-01, 2.25E-01, 4.00E-01, 6.25E-01,
            9.00E-01, 1.23E+00, 1.57E+00, 1.84E+00, 2.07E+00]
#gate-to-source voltage sweep  
VGS = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

def res(m,n):
    rsheet=25
    #Esquina sin considera
    rt=m*n*rsheet
    
    #Considerando esquina
    # rt=(m*n-1/3*(n**2+n*(n-3)))*rsheet
    return rt

def curr(vgs,W,L):
    beta=4.5e-6
    gamma=0.01
    vth=0.69
    VDS=5
    ID=beta/2*W/L*(vgs-vth)**2*(1+gamma*VDS)
    return ID


def fitness(R):
    f=0
    lmbd=0.3
    W,L,m,n=R
    W=W*lmbd
    L=L*lmbd
    for i in range(len(VR_data)):
        f+=(VR_data[i]-curr(VGS[i],W,L)*res(m,n))**2
    f=f/len(VR_data)
    return -f