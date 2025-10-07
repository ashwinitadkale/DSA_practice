# Input: N = 3
# Output: 
# * * *
# * * *
# * * *  
#code
# n=int(input())
# for i in range(n):
#     for j in range(n):
#         print('*',end=' ')
# #     print()
# ****
# ***
# **
# *
n=int(input())
for i in range(n,1):
    for j in range(i):
        print('*',end=' ')
    print()

# n=int(input())
# for i in range(n):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# n=int(input())
# for i in range(n):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()