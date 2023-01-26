#Copy List...copy()
list1=["a","b","c"]
mylist=list1.copy()
print(mylist)

#Another method is list() method..
list1=["a","b","c"]
mylist=list(list1)
print(mylist)

#Join two list...Using '+' Operator..
list1=["a","b","c"]
list2=[1,2,3]
list3=list1+list2
print("1 Method=",list3)

#Using append() method..
list1=["a","b","c"]
list2=[1,2,3]
for x in list2:
    list1.append(x)
print("2 Method=",list1)

#Extend() method...
list1=["a","b","c"]
list2=[1,2,3]
list1.extend(list2)
print("3 method=",list1)
