#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
MyScore은 5개 함수를 가지고 있는 모듈입니다.
모듈은 반드시 확장자가 py로 끝나야 한다
1) File>download as>py서택
2) 매직명령어 %%
'''


# In[ ]:


def getSum(data):
    sumD =0
    for i in data:
        sumD+=i
    return sumD

def getMean(data):
    meanD=0
    meanD = getSum(data)/len(data)
    return meanD

def getMax(data):
    maxD = data[0]
    for i in data[1:] :
        if(maxD<i):
            maxD=i
    return maxD

def getMin(data):
    minD=data[0]
    for i in data[1:]:
        if(minD>i):
            minD=i
    return minD

def getTwoSum(num2,num1=1) :
    twosum =0
    if num1>num2:
        num1, num2 = num2, num1
    for i in range(num1,num2+1):
        twosum+=i
    return twosum
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




