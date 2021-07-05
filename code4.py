#! /usr/bin/env python
###사칙연산 함수
#내 답
def calc(num0,num1,op):
    if op == "+": #덧셈
        resutl=(num0+num1)
    elif op == "-": #뺄셈
        if num0>=num1:
            result=(num0-num1)
        else:
            result=(num1-num0)
    elif op == "*": #곱셈
        result=(num0*num1)
    elif op == "%": #나눗셈
        result=(num0//num1+num0%num1)
    else:
        result=("연산기호가 올바르지 않습니다")


    return result

#강사 답
def cal(num0,num1, op):
    print('{}{}{}'.format(num0,num1,op)) #어떤 인자를 받았는지 알기위해 프린트 해준다
    if op == '+':
        result = num0+num1
        return result #계산결과가 끝났으니 return해서  바로 보여준다.
    elif op == '-':
        result = num0-num1
        return result #return: 함수 진행이 끝나서 나온다.
    return result


cal(3,4,'+')

##내장함수를 이용한 계산
print(eval('5+2')) #7이 출력됨


############################
##피보나치 수열
#앞에 두숫자를 더하면서 새로운 수열을 생성

#[0,1,1,2,3,5,8,13,21, ....]


# func ->> F_7구하기

#내 풀이
in_num =input("입력값 :")

while not in_num.isdigit():
    in_num = input("숫자로 입력하세요:")
in_num = int(in_num)

num_list = [0,1]

fivo = []
fivo_add=[]
for i in range(in_num):
    if i == 0:
        fivo.append(0)
    elif i == 1:
        fivo.append(1)
    else:
        l_sum = fivo[-1]+fivo[-2]
        fivo.append(l_sum)
    
#재귀
def clac_fivo(n):
    if n==0:
        print(0)
    else:
        print(n)
        clac_fivo(n-1)
       
'''
def clac(fn1,fn2)
    last_ans= (fn1+fn2)
    cycle = 
    print(cycle)
#값이 1개인 경우

#값이 2개 이상인 경우
#리스트 마지막 두개 값 더하기
l_sum= a[-1]+a[-2]
a.append(l_sum)

print(a) #a에 마지막 두개 값 더한거 넣어줌.


print(cycle)            
           
'''

#피보나치
#강사 풀이
#sol1
#list사용한 방법
n_pivo = int(input('n_th pivo: '))
l_pivo = [0,1] #n_th pivo : l_pivo[n]
print('len(l_pivo):', lens(l_pivo))
#use list and .append
def pivo(n):
    while len(l_pivo) <n: #l_pivo개수가 n개수보다 길이가 짧으면 
        l_pivo.append(l_pivo[-1]+l_pivo[-2])
    print(l_pivo[-1])
    print(l_pivo)
pivo(n_pivo)


##sol2
#for 사용한 방법
n_pivo = int(input('n_th pivo: '))
l_pivo = [0,1] #n_th pivo : l_pivo[n]
def pivo(n):
    for i in range(n- len(l_pivo)):
        l_pivo.append(l_pivo[-1] + l_pivo[-2])
    print(l_pivo[-1])
    print(l_pivo)
pivo(n_pivo)

#sol3
#재귀함수 이용한 방법

n_pivo = int(input('n_th pivo: '))
l_pivo = [0,1] #n_th pivo : l_pivo[n]
def pivo_r(n):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        return pivo_r(n-1) + pivo(n-2)
print("pivo_r:", pivo_r(n_pivo -1))


####################
#지역변수와 전역변수

chicken = 10 #전역변수

def countChicken(people):
    chicken = 20    #지역변수 chicken(함수 안에 쓰여서)
    chicken -= people   #chicken에서 사람 수만큼 뺐다.
    print(chicken, 'chicken remained')
def countChicken_global(people):    #global이란 명령어 사용
    global chicken      #전역변수 chicken을 가져다 쓴다.
    chicken -= people    #데이터 수정 #chicken = chicken -people 이란 뜻   
    print('{0} chicken remained.'.format(chicken))

print('chicken:', chicken)
countChicken(5)
print('chicken:',chicken)
print()
print('chicken:', chicken)
countChicken_global(5)
print('chicken', chicken)

##############
#파일 입출력
#code5.py

###########
#클래스


