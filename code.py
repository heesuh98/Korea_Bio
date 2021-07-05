#! /usr/bin/env python
A = 'red apple'
B = 'yellow banana'

#yellow apple
#red banana
'''
print(B[:7]+A[4:])
print(A[:3]+B[6:])
'''
'''
##문자열포매팅
cnt = 1
print('there are {} apple.' .format(cnt))  #문자열 .format(함수))
cnt = 'one'
print('there are {} {} apple.' .format(cnt, 'peaches')) #{}을 쓰면 어떤 형식이든 들어갈 수 있음
cntApple = 3
print('there are %d apple.' % cntApple)
cntApple = 4
print('there are %d apple.' % cntApple)
print('-' *30)

fruit = 'apples'
print('there are %s from %s tree.' % (fruit, fruit))
fruit = 'peachs'
print('there are %s from %s tree.' % (fruit, fruit))
fruit = 'plum'
print('there are %s from %s tree.' % (fruit, fruit))
'''
'''
##문자열comma 제거

CMA = '1,234,567'

#1234667
print(int(CMA.replace(',',''))+100)


#solution2
print(CMA[0]+CMA[2:5]+CMA[6:9])
'''

'''
##counting DNA Nucleotides

s = "AGCTTTTCATTCTGACTGCAACGGGCAATA\
TGTCTCTGTGTGGATTAAAAAAAGAGTGTC\
TGATAGCAGC"

print(s.count("A"),end=' ')
print(s.count("C"),end=' ')
print(s.count("G"),end=' ')
print(s.count("T"))

##transcribing DNA into RNA
DNA = 'GATGGAACTTGACTACGTAAATT'
print(DNA.replace('T','U'))
'''
'''
#list사용하기
l_test1 = [1,2,3,'apple', ' ']
l_test2 = ['a','b','c']
print(l_test1)
print(l_test1[1:])
print(l_test1[0] + l_test1[2])
print(l_test1 , l_test2)
print(l_test1 + l_test2)
print(l_test1 * 3)

l_test3 = [1,2,3,4,['a','b'],5]
'''
'''
#list중첩
myList = []
numbers = [1,2,3]
print(numbers[1])
print(numbers[1] + numbers[2])
print()
print(numbers[-1])
print("numbers[1]:", numbers[1])
print("numbers[-1]:", numbers[-1])
print("numbers[::-1]:", numbers[::-1])
'''
'''
listList = [1,2, ['one', 'two', 'three', 4]]
print(listList)
print(listList[-1][1]) #two
print()
print(listList[1:3])
print(listList[1:])
print(listList[:1])
print(listList[2][2])
'''

'''
#::이란 무엇인가
numbers = [0,1,2,3,4,5,6,7,8,9,10]
print("numbers[::1]:", numbers[::1])
print("numbers[::2]:", numbers[::2])
'''

'''
#list값 수정
num = [1,2,3,4]
print(num)
num[1] = 6
print(num)
'''
'''
###list함수
#append
l_num = [0,1,2,3]
print(l_num)
l_num.append('five')
print(l_num)


#remove

l_num = [0,1,2,3]
print(l_num)
l_num.remove(['a','b'])
print(l_num)
'''
'''
#reverse
l_num = [0,1,2,3,5,4]
print(l_num) #순서대로 list해준다
print(l_num.reverse())

print(l_num)
print(l_num.index(4)) #4의 index의 번호를 알려준다
print(l_num[4]) #4번째 index를 출력해줌

print(l_num.count(1)) #1의 갯수를 count하라
print(l_num.extend(['a','b']) #뒤에 붙는다.(추가해주기)

'''
'''
#리스트 함수연습
num = [1,2,3,4]
print(num)
num[1] = 6
print(num)
del num[2:]
print(num)
num.append(3)
print('append 3 :', num)

#pop
num = [1,3,6,7]
print(num)
print(num.pop(1))
print(num.pop())
print(num.pop(0))
'''
'''
#list만들기
lang0 = ['Python', 'JAVA']
lang1 = ['C','C++','VB']

totalLang = lang0 + lang1
print(totalLang)

#sol2
lang0 = ['Python', 'JAVA']
lang1 = ['C','C++','VB']
totalLang = lang0
totalLang.extend(lang1)
pring(totalLang)
'''

'''
###튜플(tuple): 괄호를 사용해서 선언
t_num = (1,2,3,'a')
print(type(t_num))
print(t_num)

print(t_num[0])
print(t_num[0:3])
t_num[1]=5  #튜플은 수정이 불가하므로 오류생김
print(t_num)
'''

'''
### 딕셔너리
d_table = {'fruit':'apple','color':'red','dia':10}
print(d_table['color'])
d_table['color'] = 'orange' #딕셔너리는 수정이 가능하다.
print(d_table['color'])
print(d_table)

print(list(d_table.items()))
print(list(d_table.items())[1])
print(type(list(d_table.items())[1]))
print(list(d_table.items())[1][1])

print(d_table.get('fruit'))
print(d_table['fruit'])
'''

##딕셔너리 활용

regNum0 = '951213-0000000'
regNum1 = '960125-0000000'
regNum2 = '970705-0000000'

#Dec
prt0 = {'01':'Jan', '07':'Jul', '12':'Dec'}

#Dec-13
print(prt0[regNum0[2:4]]+'-'+regNum0[4:6])
#최종

print('regNum0:',prt0[regNum0[2:4]]+'-'+regNum0[4:6])

#final

print('regNum0:',prt0[regNum0[2:4]]+'-'+regNum0[4:6])
print('regNum1:',prt0[regNum1[2:4]]+'-'+regNum1[4:6])
print('regNum2:',prt0[regNum2[2:4]]+'-'+regNum2[4:6])
