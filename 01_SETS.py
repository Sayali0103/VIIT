a = {1,2,4,5,1}#no repetative items allowed
print(a)
print(type(a))
#b = {} #it is not a empty set it becomes dictionary
#print(type(b))
#empty set can be created as
#c = set()
#print(type(c))

#LIST CANNOT BE INSERTED INSIDE A SET AS IT IS MUTABLE AND SET IS NOT MUTABLE
b = set()
print(type(b))
b.add(4)
b.add(5)
b.add((4,5,6))
print(b)
