# -*- coding: utf-8 -*-
"""

@author: Tushar_Dalvi
"""

def fun(n):
    
    arr=list(str(n))
    cnt=[0]*10
    a,b=0,0
    for i in arr:
        cnt[int(i)]+=1
    for i in range(10):
        if cnt[i]!=0 and cnt[i]!=i:
            return False
        if cnt[i]>0:
            if i%2==0:
                a+=1
            else:
                b+=1

    return a==b

n=int(input("Enter the Number:"))

while fun(n)==False:
    n+=1

print(n)               
                             
            