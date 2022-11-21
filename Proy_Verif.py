import numpy as np
from matplotlib import pyplot as plt

#Resistor voltage measured/simulated data
VR_data = np.array([1.00E-07, 2.50E-02, 1.00E-01, 2.25E-01, 4.00E-01, 6.25E-01,
            9.00E-01, 1.23E+00, 1.57E+00, 1.84E+00, 2.07E+00])
#gate-to-source voltage sweep  
VGS = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])

#fixed parameters
VDS = 5         #drain-to-source voltage  
VT = 0.69       #treshold voltage (for silicon)
beta = 4.5e-6   #transistor's beta 
rsq = 25        #sheet resistance, ohms per square

#transistor variables
W = 8.1e-6        #gate width
L = 15.6e-6        #gate length
print('W: '+str(round(1e6*W,1))+'μm\t'+'L: '+str(round(1e6*L,1))+'μm')

#resistor
m = 63          #resistor squares per line
n = 66          #resistor lines
R = 103950          # R(rsq, m, n)
print("R:", R, 'Ω')

#transistor's drain current I_D (for each V_GS value)
#resistor voltage V_R = I_D * R
# VR = []
# for i in range(len(VGS)):
#     if VGS[i] <= VT:
#         ID = 0.0
#     else:
#         ID = 0.0
#     VR.append(R*ID)

VR=R*beta/2*W/L*(VGS-VT)**2*(1+0.01*VDS)
# # mean square error
MSE = (np.sum((VR-VR_data)**2))/len(VGS)

print("mean sq error: ", round(MSE, 7))



plt.figure(1)
plt.plot(VGS,VR_data)
plt.plot(VGS,VR)
plt.grid()
plt.legend(['data','calculated'])
plt.title('$V_R$ vs $V_{GS}$')
plt.ylabel('resistor voltage (V)')
plt.xlabel('gate-to-source voltage (V)')

plt.show()

