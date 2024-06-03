import numpy as np

def costf(w,x,y):
    yp=w.T@x # 여기에 step_function을 넣을 수도 있음. yp=step_func(w.T@x)  근데 밑의 문제와 마찬가지로 불안정함.. 그래서 안넣음
    #print(yp) # 확인을 위해 넣음
    #print(y) # 확인을 위해 넣음
    return (yp-y.T)@(yp-y.T).T

def gradJ(w):
    return np.array([8*w[0]+4*w[1]+4*w[2]-4,4*w[0]+4*w[1]+2*w[2]-4,4*w[0]+2*w[1]+4*w[2]-4])

def step_func(x):
    y = x>0
    return 2*y.astype(int)-1

xi=np.array([[1,1,1,1],[0,1,0,1],[0,0,1,1]])
yi=np.array([[-1],[1],[1],[1]])
wi=np.array([[0],[0],[0]]) 

alpha=0.01
J=costf(wi,xi,yi)

while(True):
    JP=J
    delw = alpha*gradJ(wi)
    wi = wi - delw # 방향이 반대로. +로 하면 무한대로 감..
    J=costf(wi,xi,yi)
    print(J,wi.T,step_func(wi.T@xi)) # wi.T@xi 는 prediction value. 이를 정확하게 하려면 step function을 넣으면 됨
    if(np.abs(J-JP)/J < 0.000001) : break
    
#step_func의 단점..
#-0.0000001 이라도 -1로 분류하기 때문에. 오류가 발생될 수 있다.

#내가 항아리의 어느 지점을 가리키든 (초기값이 어떻든 간에)
#cost function과 cost function의 기울기만 알면, (J와 gradient J만 알면)
#항아리의 바닥이 어딘지 알 수 있다! (결과를 알 수 있다.)
#길이 다를 뿐 목적지는 같다는 뜻이다.
