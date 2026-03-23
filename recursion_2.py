# #Factorial of a given number
# def fact(n):
#     if n==0 or n==1:  
#         return 1
#     return n*fact(n-1)

# #input
# N=int(input())
# print("factorial of n",fact(N))

# #reverse an array
# def rev_arr(a,i,j):
#     if i>=j:
#         return
#     a[i],a[j]=a[j],a[i]
#     rev_arr(a,i+1,j-1)
# #input
# arr=[1,2,3,4,5,6]
# rev_arr(arr,0,len(arr)-1)
# print(arr)

def is_palindrome(s, left, right):
    if left >= right:   # Base case
        return True
    
    if s[left] != s[right]:   # Mismatch
        return False
    
    return is_palindrome(s, left+1, right-1)

# Input
s = "madam"
print(is_palindrome(s, 0, len(s)-1))






