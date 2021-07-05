#! /usr/bin/env python
'''
print(set([1,2,3,5,4,4,3,4,4,4]))

mySet = {'a','b','c'}
print(mySet)
'''
'''
setA = {2, 4, 6, 8, 10, 12}
setB = {9, 3, 12, 6}

print( setA | setB )
print( setA & setB )
print( setA - setB )
print( setA ^ setB )

setA |= {100} #setA에 100을 추가한다
print(setA)

print(set.union(setA, setB))
print(setA | setB) #위에 명령이랑 동일한 결과 나옴

#union
setA = {2, 4, 6, 8, 10, 12}
setB = {9, 3, 12, 6}
setC = {'j','b'}
print( set.union(setA,setB,setC))
print(setA | setB | setC)
'''
'''
#불리언
print(True, False)

print(bool('aa'))

print( 1<10 )
'''


#################################
##사용자 입력
'''
print() #그냥 공백
myVar = input('Please input string: ')
print(myVar)
'''
'''
myVar1 = input('Var1: ')
myVar2 = input('Var2: ')
myVar3 = input('Var3: ')

print()
print(myVar1)
print(myVar2)
print(myVar3)
'''
'''
########################
myVar1 = input('Var1:')

if myVar1 == '1':             ##조건문의 참 거짓을 통해 데이터를 다르게 처리함
    print('myVar1 is 1!')    ##input시 string으로 인식한다
else:
    print('myVar1 isnt 1!')
print('Good Bye!')
'''
'''
###################
#큰수 출력하기

num0 = 5
num1 = 7

if num0>num1:
    print(num0)
else:
    print(num1)

#sol2
print(num1) if num0 < num1 else print(num0) #한줄에 써도 된다.
'''
'''
##########################
#elif문

fruit = 'Apple'

if fruit == 'peach':
    print('peach')
elif fruit == 'apple':
    print('apple')
else:
    print('else~~~')

#####################
'''
'''
######################
##등급 지정하기
#input사용해 학점입력하고 elif 사용해서 등급 출력하기

#나의 정답
score = int(input('score: ' )) #input하면 string으로 받기 때문에 int로 바꿔주기

#101이상 0이하 grade 없다고 지정

if 100 >= score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(grade)


##정답

score = input('score: ')
score = int(score)
if (score<100) and (score >= 90):
    grade ='A'
elif (score<90) and (score >= 80):
    grade ='B'
elif (score<80) and (score >= 70):
    grade ='C'
elif (score<70) and (score >= 60):
    grade ='D'
elif (score<60):
    grade ='F'
else:
    grade = 'Incorrect score'

print(grade) #grade라는 변수 만들어서 저장한번 해주고 하기.

'''
'''
##########
#환율계산기

#나의 풀이 --망함
inStr = '10 USD, 5 EUR, 7 JPY, 9 CNY'

d_value = {
            'USD' : 1203.82,
            'EUR' : 1365.73,
            'JPY' : 11.22,
            'CNY' : 172.04
            }
inStr.split(',')

a= inStr.split(',')
print(inStr.split(','))

print(a[1][2:6])


outStr=float( inStr[:2]) *float( d_value.(a[1][2:6]))
print(outStr)



#EUR을 얻었으니 이걸 DIC으로 가져와서 VALUE를 가져온다.
print( d_value[b] )

outStr

print( outStr )
'''
'''

###답
d_value = {
            'USD' : 1203.82,
            'EUR' : 1365.73,
            'JPY' : 11.22,
            'CNY' : 172.04
            }

inStr = inStr.split(',') #, 로 나누기

print( (inStr[0].strip().split())) #strip: 앞뒤  공백없애기, split: 문자열 공백기준 나누기
VALUE0 = (inStr[0].strip().split()[0])
TYPE0 = (inStr[0].strip().split()[0])
VALUE1 = (inStr[1].strip().split()[0])
TYPE1 = (inStr[1].strip().split()[1])
VALUE2 = (inStr[2].strip().split()[0])
TYPE2 = (inStr[2].strip().split()[1])
VALUE3 = (inStr[3].strip().split()[0])
iTYPE3 = (inStr[3].strip().split()[1])

print(VALUE0, VALUE1, VALUE2, VALUE3)
print(TYPE0, TYPE1, TYPE2, TYPE3)

RESULT0 = round(int(VALUE0) * d_value[TYPE0], 3)
RESULT1 = int(VALUE1) * d_value[TYPE1]
RESULT2 = int(VALUE2) * d_value[TYPE2]
RESULT3 = int(VALUE3) * d_value[TYPE3]

print(inStr[0].strip().split())


outStr = inStr[0].strip().slit()[0]*


RESULT0 = int(VALUE0) *int( d_Value[TYPE0]) #string 을 int로 바꾼다

print(VALUE0, VLAUE1, VLAUUE2, VLAUE3)
print(TYPE0, TYPE1, TYPE2, TYPE3)

#join 함수 써서 답이랑 똑같이 출력하기(값 사이사이에 KRW, 를 넣어주고 맨 마지막엔 KRW추가)
outStr = 'KRW, '.join([RESULT0,RESULT1, RESULT2, RESULT3]) + 'KRW'

#%f이용
print(
'''

################
#while문
'''
i = 1
while i < 11:
    print('loot test: ' + str(i))
    i += 1
'''

##
i = 1
while True :
    print('loop test: ' + str(i))
    i += 1
    if 50 < i :
        break


