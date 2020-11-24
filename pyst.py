import numpy as np
def st(x):
    # S变换。输入为numpy的实矩阵，输出为numpy的复矩阵
    H = np.fft.fft(x)
    n=len(x)
    t=np.append(np.arange(np.ceil(n/2)),np.arange(-np.floor(n/2),0))
    t2=np.reciprocal(t[1:])[None]
    t=t[None].T
    t3=np.matmul(t, t2)
    t4=np.exp(-2*np.pi*np.pi*np.power(t3,2))
    t5=np.zeros([n,1])
    t5[0]=1
    t6=np.append(t5,t4,axis=1)
    t7=H[None]
    tt=np.arange(0,n)
    for i in range(1,n):
        t7=np.append(t7,H[np.roll(tt,-i)][None],axis=0)
    return np.fft.fft(np.fft.ifft2(t6*t7)).T

def main():        
    a = np.array([1,-1,2,-1,1,-6,2,-1])
    y = st(a)
    print(y)
    
if __name__ == '__main__':
    main()





