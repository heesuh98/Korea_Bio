#! /usr/bin/env python

#while문을 이용한 삼각형 출력하기

i=0
while i<7:
    print('*'*i)
    i += 1

#####답
i = 1
while True :
    print('*' * i)
    i += 1
    if 7<i :
        break

#####sol2
#덧셈 이용하기

star = ''
while True :
    print(star)
    star += * #*을 하나씩 star라는 변수에 더함
    if 7 < i:
        break

 
