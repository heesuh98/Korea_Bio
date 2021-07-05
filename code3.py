#! /usr/bin/env python
'''
##for
for i in [1,2,5]:
    print(i)
print('done!')

#변수설정
l_range = [1,2,5] #list

for i in l_range:
    print(i)
print('done!')

#변수 i, a 설정
l_range = [1,2,5] #list
i = '*'
for a in l_range:
    print(a)
    print(i)
print('done!')

#for문 안에 if문
#for문 에는 indent된게 와야한다

l_range = [1,2,5] #list
for i in l_range:
    if i == 1:   #indent required
        print(i)

print('done')

#

l_range = [1,2,5,3,1,7] #list
for i in l_range:
    print('current i:' , i)  #i가 뭔지 체크한다
    if i == 1:   #현재 i가 1인 경우
        print(i)
    else :           #현재 i가 1이 아닌경우
        continue #continue:아무것도 하지 말고 넘어가라
    print('current i:' , i) 

print('done!')

#range
for i in range(2):
    print("*")

#range 범위지정
print ('0123456789'[0:5:1])
print(list(range(0,5,1)))
print(list(range(2,5,1))) #2부터 시작해서 5전까지 1씩 증가
print(list(range(9)))

#
totalSum=0
for i in range(0,3,1):
    totalSum += i
    print(i)

print('totalSum:', totalSum)

#pass와 continue차이
##continue는 for로 돌아간다
###pass는 그냥 코드 무시하고 지나친다
for i in range(3):
    if i ==2:
        print(i)
    else:
        continue
    print('current i:' , i)

#########
#내장함수
all ([True, False])
all ([False, False])
all ([True, True])

'''
'''
#############
##구구단 출력

gugu =input('gugu? ') #input받으면 str형식. 

while not gugu.isdigit():  #숫자형이 아니면 입력 잘못되었다고 출력
    gugu = input ('gugu is not digit:') #숫자가 아니면 계속 while문 반복

gugu = int(gugu) #gugu를 int로 변경(input은 str이므로)

while not (2<= gugu <=19):         #범위 지정
    
    gugu = input('[2,19]:')
gugu = int(gugu)

for i in range (1,10):
    dan = i * gugu
    print('{} * {}: {}'.format(gugu, i, dan))

'''

'''
#####################
#sum of all odd from 'a' through 'b'
num1 = input('put number :')
num2 = input('put another number: ')

while not num1.isdigit():
    num1= input('num is not digit:')

num1 = int(num1)
num2 = int(num2)


for i in range(num1, num2):
    if i %2 ==1:
        print(sum([num1,num2]))
    else:
        print("please put odd number")

#홀수만더하기 정답
inStr = input('a,b:')
a, b = inStr.split

myList = []
for i in range(int(a), int(b)):
    if i % 2 == 1:
        myList.append(i)
    print(myList)
print(sum(myList))
'''

#############3
##palindromic sequence판별
##틀림..ㅎㅎ
#sequence == resverse complement
'''
DNA = input("write DNA: ")

while not DNA.isalpha():
    DNA= input('num is not string:')

list(DNA)
(',').join(string.split())
print(nDNA = DNA.split(','))
'''
'''
##
##최종답
a =input('DNA? ') #input받으면 str형식.
DNA = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
result = [] 
for i in reversed(a): 
    result.append(DNA[i])
lastDNA = (''.join(result))

if lastDNA == a:
    print(lastDNA, "is palindromic.")
else:
    print(lastDNA, "is not palindromic.")

#######
##정답
inSeq = input('give me sequence: ')
d_nuc1 = {'A':'T','T':'A', 'G':'C', 'C':'G'}
outSeq = ''

for i in range(len(inSeq)): #01234~
    print(inSeq[i]) #앞에서부터 읽기
    print(inSeq[-i-1]) #뒤에서부터 읽기
    print(inSeq[-(i+1)]) #



#####
'''
'''
###
#DNA Nucleotide

#정답
toCount = 'We tried list and we tried dicts also we tried Zen'

d_Count = dict()
l_toCount = toCount.split()
for i in l_toCount: #단어 리스트
    print(i.strip()) #단어 확인

    if key not in d_Count: #딕셔너리 키 유무확인
        d_Count[key] = 1 #없으면 1
    else:
        d_Count[key] += 1 #있으면 +1

for i in d_Count:
    print(i, d_Count[i])

for k, v in d_Count.items():
    print(k, v)


print(d_Count)

######
#sol2
#counter이용한 답(이미 존재하는 라이브러리 사용함)

from collections import Counter

toCount ='We tried list and we tried dicts'

l_toCount = toCount.split()
cnt = Counter(l_toCount) #list형식으로 cnt에 넣는다 #dic이랑 똑같다!
print(cnt)
cnt['tried'] += 100 #100을 더함
print(cnt)

#################

'''
'''
if 'and' in d_dict :
     print('theres and!') #dic안에 and라는 key가 있는가? 있으면 print

d_dict.get('and')

d_dict['and'] =1

if 'and' in d_dict: print('theres and!')

d_dict.get('and') #and에 따른 value를 가져와

d_dict['and'] += 1 #dic안에 and를 불러와서 1을 더함. 1+1 =2

##정답
#dic을 사용해서 단어개수 세기
#key가 딕셔너리에 없으면 1
#key가 딕셔너리에 있으면 +1

toCount = 'We tried list and we tried dicts also we tried Zen'

l_toCount = toCount.split()

'''

# d_Count= print(input("dict:"))


##########
#함수

def showHello():
    print('Hello')
    return '1'

a = showHello()
print('number?')
print(a)

#
def showHello():
    print("hihi")
    return '1'

print(showHello())
print(showHello())

##
def add(a,b):
    print('add',a,'and',b)
    print('%d+%d='%(a,b),a+b)
    return a+b

result = add(3,4)

print('result:',result)

###
#매개변수
def hello() -> None: #화살표를 사용해서 값을 표현한다.
    print('hello!!')

hello()

def add(a,b) -> int: #단, 화살표는 파이썬 3.9버전 이상에서만 사용하자.
    return a+b 

##
def add(a,b = 3):
    return a+b

print(add(3,4))
print(add(3))

##
def book_0(name, age, book1, book2):
    print('name: {0} age: {1}'. format(name, age), end = '')
    print('book:', book1, book2)

def book_1(name, age, *books):
    print('name: {0} age: {1}'.format(name, age), end =' ')
    print('book:', end = ' ')
    for book in books:
        print(book, end = ' ')
    print()

book_0('yune', 5, 'python', 'basic')
book_1('yune', 5, 'python', 'basic')
book_1('yune', 5, 'python', 'basic','photo')

book_0('yune', 5, 'python', 'basic', 'photo') #error #가변매개변수를 사용하면 오류 안난다.
#람다
print((lambda a, b : a+b) (3,4))

def add(a,b): return a+b

print(add(3,4))


