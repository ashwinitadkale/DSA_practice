# Input: N = 3
# Output: 
#1
# * * *
# * * *
# * * *  
#code
n=int(input())
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()
#2
# * 
# * *
# * * *
# * * * *
# * * * * *

n=int(input())
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()
#3
# 1
# 1 2
# 1 2 3
n=int(input())
for i in range(n):
    for j in range(1,i+1):
        print(j,end=' ')
    print()