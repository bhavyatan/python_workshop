
myset={1,2,3,6}
myset1={2,34,3}
myset2={}

#adding , removing 
'''
myset.add(4)
myset.remove(2)
print(myset)
'''
'''
for x in myset:
    for y in myset1:
        if x==y:
            print(x)
            break
'''
# add,remove,union,distort

#union of two sets
myset2=myset.union(myset1)
print(myset2)

#intersection of two sets
myset2=myset.intersection(myset1)
print(myset2)

#diff of sets
myset2=myset.difference(myset1)
print(myset2)