# a=(1,45,456,6789,False,"Fatima","Ali")
# n0o=a.count(45) # it will return tuple like string in this case we we will be able to find occurence of the (45)-->1
# index=a.index(1) # 1 is located on which position
# print(no)
# print(index)

t = (4, 2, 7, 2, 9, 2)
count=t.count(4)
ind=t.index(9) # 9 is located on which index
print(count)
print(ind)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))

# Conversion of list into tuple
my_list = [10, 20, 30]
my_tuple = tuple(my_list)
print("Tuple from list:", my_tuple)
tuple1=(1,2,3)
tuple2=(4,5,6)
concatenation=tuple1+tuple2
print(concatenation)

# Repitition
tuple1=(1,2,3)
rep=tuple1*3
print(rep)

# Memebership
t = (1, 2, 3, 4, 5)
print(1 in t)
print(3 not in t) #output=true,false

# Slicing in tuplets
t = (1, 2, 3, 4, 5)
print("Slice from index 1 to 3:", t[1:4])  # Output: (2, 3, 4)

# sq of nos by looping thorugh method
nums = (2, 4, 6)
for n in nums:
    print(n * n)
    
    # cubing
    cube=(1,2,3)
    for c in cube:
        print(c*c*c) #Output=1,8,27
       
        # tuple unpacking assigning value to seperate variables
        tp = (1, 2, 3)
        a, b, c = tp
        print(a, b, c) # a=1,b=2,c=3


