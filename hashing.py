# Frequency Count 
arr=[1,2,1,3,2,1]
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print(freq)

# Character Hashing 
s='ashwini'
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
print(freq)

#Check Element Exists
arr=[10,20,30,40]
hash_set=set(arr)
print(20 in hash_set)
print(50 in hash_set)

# Count Distinct Elements
arr=[1,2,2,3,3,3]
distinct=set(arr)
print(len(distinct))

#Highest Frequency of Element
arr=[1,2,1,3,2,1]
freq={}
for num in arr:
    freq[num]=freq.get(num,0)+1
max_freq=0
element=None

for key in freq:
    if freq[key]>max_freq:
        max_freq=freq[key]
        element=key
print("Element:",element,"Frequency:",max_freq)