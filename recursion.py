# def print_name(n):
#     if n == 0:   # Base case
#         return
#     print("Ashwini") 
#     print_name(n-1)    # Recursive call


#Print 1 to N using recursion
def print_num(n):
    if n==0:
        return
    print_num(n-1)
    print(n)

#sum of first N numbers
def sum_n(n):
    if n==0:
        return
    return n+sum_n(n-1)


#input
N = 5
print(sum_n)
# print_num(N)
# print_name(N)


