#!/usr/bin/env python
# coding: utf-8

# # 2. 함수
# ## Background
# - 함수
# - 모듈
# 
# ## Problem
# ### 1. myGame 모듈(파일명 : myGame.py)을 만들고 그 안에 아래의 2개 함수를 선언하세요.
# #### 첫 번째 함수 - 랜덤한 숫자 6개를 받아 출력하는 lotto 함수를 구현해보세요
# - 함수 이름은 makeLotto(num)로 하세요.
# - random.randrange() 함수를 사용해서 1부터 45까지의 값을 발생시켜서 6개의 로또번호를 출력합니다.(중복은 제외하고 6개를 출력하세요)
# - ex) [1, 4, 25, 26, 30, 40]
# - 테스트 코드 내에서 함수의 인자 값으로 전달받은 값만큼 로또 게임을 출력하세요.
# - ex) 2를 인자값으로 전달받으면 로또 2게임을 생성합니다.
# - 게임 1 [1, 4, 25, 26, 30, 40]
# - 게임 2 [4, 7, 15, 23, 35, 41]
# 
# #### 두 번째 함수 - 학점들을 입력받아서 그 학점들의 평균을 출력하는 함수를 구현해보세요.
# - 함수 이름은 meanGrade(grade)로 하세요.
# - 테스트 코드 내에서 함수의 인자 값으로 전달받은 학점들을 ','를 기준으로 나눠서 학점들의 평균을 계산하세요.
# - 학점에 따른 점수는 다음과 같습니다.
# - A+ : 4.5, A : 4.3, A- : 4.0, B+ : 3.5, B: 3.3, B-: 3.0, C : 2.5, D : 1.5
# - ex) "A+,A-,B+" 를 인자값으로 전달받으면 학점 평균을 계산해서 출력합니다.
# - 평균 : 4.0
# 
# ### 2. 선언된 함수를 다른 테스트 파일(TestModule1.ipynb)에서 import해서 기능을 테스트 해보세요.
# ### 그 후 최종적으로 위의 두가지 함수 중 원하는 것을 골라서 실행시킬 수 있는 함수를 만들어보세요

# In[32]:


import random
def makeLotto(num):
    for turn in range(num):
        repeat=0
        numL=[]
        while len(numL) <7:
            #print(numL)
            ranNum= random.randrange(1,46)
            #print(ranNum)
            numL.append(ranNum)
            a=set(numL)
            numL=list(a)
            repeat=repeat+1
        print('게임',(turn+1),numL)


# In[50]:


def meanGrade(grade):
    gradeDic = {'A+' : 4.5, 'A' : 4.3, 'A-' : 4.0, 'B+' : 3.5, 'B': 3.3, 'B-': 3.0, 'C' : 2.5, 'D' : 1.5}
    gradeL = grade.split(',')
    gradeSum=0
    for grade in gradeL:
        gradeSum+=gradeDic.get(grade)
    return round(gradeSum/len(gradeL),1)


# In[ ]:


def whichFunction():
    choice = int(input('어느 함수를 실행하시겠습니까? 1:로또 게임, 2:학점계산기'))
    if(choice==1):
        num= int('게임을 몇 번 할 지 숫자로 알려주세요')
        makeLotto(num)
    else:
        grade = input('학점을 ,단위로 입력해주세요')
        meanGrade(grade)

