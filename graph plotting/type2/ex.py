
import numpy as np
import matplotlib.pyplot as plt

w,x,y,z=np.loadtxt("plot_data_i3.txt",unpack=True,dtype=str)

a,b,c,d=np.loadtxt("parsed_data.txt",unpack=True,dtype=str)
#for first data#
tmp1=np.array(x)
x=tmp1.astype(np.float)
tmp2=np.array(y)
y=tmp2.astype(np.float)
tmp3=np.array(z)
z=tmp3.astype(np.float)
#for parsed data#
tmp4=np.array(b)
b=tmp4.astype(np.float)
tmp5=np.array(c)
c=tmp5.astype(np.float)
tmp6=np.array(d)
d=tmp6.astype(np.float)
plt.subplot(2,2,1)

plt.xlabel('t')
plt.ylabel('v1')
plt.plot(x,y,'r')
plt.legend(['t vs v1'])
plt.subplot(2,2,2)

plt.xlabel('t')
plt.ylabel('v2')
plt.plot(x,z,'g')
plt.legend(['t vs v2'])
plt.subplot(2,2,3)

plt.xlabel('t')
plt.ylabel('v3')
plt.plot(b,c,'b')
plt.legend(['t vs v3'])
plt.subplot(2,2,4)

plt.xlabel('t')
plt.ylabel('v4')
plt.plot(b,d,'r')
plt.legend(['t vs v4'])
plt.savefig('plot v1-v2-v3-v4.png')

