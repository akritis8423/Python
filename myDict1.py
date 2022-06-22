# d={2:4,66:"erf",99:"pqrst"}
# print(d[99])

# #creatinga dictionary
# dict={4:44,5:55,6:66,7:77}
#
# #deleting a key
# #using pop() method
# m=dict.pop(4)
# print(m)
# print(dict)


# #creatinga dictionary
# dict={4:44,5:55,6:66,7:77}
# m=dict.popitem()            #deleting key using popitem
# print(m)
# print(dict)


# # creatinga dictionary
# dict={4:44,5:55,6:66,7:77}
#
# #deleting a key
# #using pop() method
# m=dict.get(7)
# print(m)
# print(dict)



# # creatinga dictionary
# dict={4:44,5:55,6:66,7:77}
#
# #copying dictionary
# #using copy() method
# m=dict.copy()
# print(m)
# print(dict)



# # creatinga dictionary
# dict={4:44,5:55,6:66,7:77}
# #copying dictionary
# #using copy() method
# m=dict.copy()
# # print(id(m))
# # dict[5]=678
# print(m)
# print(id(dict))
# print(id(m))



# creatinga dictionary
# dict1={4:44,5:55,6:66,7:77}
# dict2={3:44,4:55,5:66}
#
# #updating dictionary by another dictionary
# #using update() method
# dict1.update(dict2)
#
# print(dict1)



# # creatinga dictionary
# dict1={4:44,5:55,6:66,7:77}
# #updating dictionary with iterable
# #using update() method
# print(dict1)
# dict1.update({3:44,2:33})
# print(dict1)


# # creatinga dictionary
# dict1={4:44,5:55,6:66,7:77}
#
# #updating dictionary by
# #using setdefault() method
# dict1.setdefault(8,88)
#
# print(dict1)



# # creatinga dictionary
# dict1={4:44,5:55,6:66,7:77}
#
# #updating dictionary by
# #using setdefault() method
# m=dict1.setdefault(6)
# print(m)
# print(dict1)


# # creatinga dictionary
# dict1={4:44,5:55,6:66,7:77}
# #using keys() method
# m=dict1.keys()
# print(m)
# print(dict1)


# # creatinga dictionary
# dict1={4:44,5:55,6:66,7:77}
# #using keys() method
# m=dict1.keys()
# print(m)
# dict1.clear()       #clear the dictionary
# print(dict1)


# # creatinga dictionary
# dict1={4:44,5:55,6:66,7:77}
# dict2={3:77,9:76,8:99}
# #using keys() method
# m=dict1.keys()
# print(m)
# print(id(m))
# dict1.update(dict2)
# m=dict1.keys()
# print(dict1)
# print(m)
# print(id(m))



# # creatinga dictionary
# dict1={4:44,5:55,6:66,7:77}
# # #using items() method
# m=dict1.items()
# print(m)
# print(type(m))
# for e in m:
#     print(e)
#     print(type(e))
# for e in m:
#     print(e[0])
#     print(e[1])                # unpacking's concept



# # creatinga dictionary
# l1=[3,4,5,6]
#
# #using fromkeys() method
# m=dict.fromkeys(l1)
# print(m)
# l2=[1,2,3,4]
# i=0
# for e in m:
#     m[e]=l2[i]**2
#     i+=1
# print(m)


# #WAP to make dictionary using  two lists
# #creating list
# l1=[1,2,3,4]
# l2=[3,4,5,6]
# d={}               #creating empty dictionary
# for i in range(len(l1)):
#     d.update({l1[i]:l2[i]})     #adding items to empty dictionary
# print(d)



# #WAP to make dictionary using one list and string
# #creating list
# l1=[1,2,3,4]
# str="cetpa"
# d={}               #creating empty dictionary
# for i in range(len(l1)):
#     d.update({l1[i]:str[i]})     #adding items to empty dictionary
# print(d)



