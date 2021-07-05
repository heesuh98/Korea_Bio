#! /usr/bin/env python

FILE = open('./test_file.txt', 'r')

for i in FILE.readlines():
    print(i.strip().split()[0])  #split으로 나누고 0번인덱스만 가져오기

FILE.close()

#파일 쓰기
FILE = open('./write_file.txt', 'w')

for i in ['I', 'like', 'apple']:
    FILE.write(i+ ' ')
FILE.write('\n')

FILE.close

#with문으로 open하기
with open('./test_file.txt', 'r')as FI, open('./write_file.txt', 'w')as FO:
    for i in FI. readlines(): #readlines로 리스트 끝까지 읽는다
        print(i.strip())
    print('with out! BYE!')
print('hi')

#pickle
import pickle
l_list = [1,3,5,7]


