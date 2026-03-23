def print_name(n):
    if n == 0:   # Base case
        return
    print("Ashwini") 
    print_name(n-1)    # Recursive call


#Print 1 to N using recursion
def print_num(n):
    if n==0:
        return
    print_num(n-1)
    print(n)

#sum of first N numbers
def sum_n(n):
    if n==1:
        return 1
    return n+sum_n(n-1)


#input
N = 5
print("sum of first N integers is:",sum_n(N))
print("print 1 to N numbers:",print_num(N))
print("print name N times",print_name(N))


