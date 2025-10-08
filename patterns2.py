# ****
# ***
# **
# *
# n=4
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=' ')
#     print()

# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2 
# 1
n=6
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(n-j+1,end=' ')
    print()