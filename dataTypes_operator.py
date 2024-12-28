'''
print("Hello Wolrd")
userVar=input("Enter String: "); y=50
print(f"y = {y}")
print("y=",y)
floatX=float(input("Enter Float Value : "))
print(f"float value is {floatX}")
a=b=c=80
print(f"a={a}, b={b},c={c}")
ax,bx,cx=50,20,3.5
print(f"ax={ax} ,bx={bx} ,cx={cx}")
'''

#Perform arithmatic operation on 'a' and 'b' and print result
'''a=10
b=20 
print(a+b)  '''
int_var=10
float_var=20.5
string_var="Hello"
bool_var=True

#List are mutable
list_var=[44,55,66,77]
#print(f"list = {list_var}") #; print(f"list_index1= {list_var[1]}")
#print(f"list = {list_var[:]}");print(f"list ind1to3= {list_var[1:4]}")
#print(f"list = {list_var[-1]}")
#print(f"list2 = {(list_var[-3: ])}")
#print(f"list3 = {(list_var[-1: -4 : -1 ])}")
# list_var[1:]=(1,2,3)
# print(f"list {list_var}")

# list_var.append(7)
# list_var.extend([99,88,45,99])
# list_var.insert(2,75)
# list_var.remove(75)
# list_var.pop(2)
#list_var.sort()
list_var.reverse()
#list_var.sort()
#print(f"list {list_var}")

#tuple are immutable
tuple_var=(11,77,77,22,44)
# print(f"Tuple is  {tuple_var+(12,55)}") #it will return new tuple becz it is immutable
# print(f" 22 present at index: {tuple_var.index(77)}")
# print(tuple_var.count(77))

#set accept only unique values.It does not follow indexing
# set_var={44,88,22}
# print(f"set is {set_var}")
# set_var.add(5)
# set_var.discard(88)
# union_set=set_var.union({44,22,66})
# print(f"union set is {union_set}")
# set_difference=set_var.difference(union_set)
# print(f"set difference is {set_difference}")

#In dictionary data are stored in key-value pair where key and value are any datatype.Key is immutable.
dict_var={1:'A','B':2}
print(f"Dictionary = {dict_var}")
dict_var['C']=3
print(f"Added new key value in Dictionary = {dict_var}")
dict_var[1]=44
print("Updated Dictionary key 1 ={dict_var}")
dict_var.pop('C')
print(f"remove Dictionary key C = {dict_var}")
keys=dict_var.keys()
values=dict_var.values()
items=dict_var.items()

a=20;b=50
#Arithmetic Operators
print(f"{a}+{b}={a+b}"); print(f"{a}-{b}={a-b}")
print(f"{a}x{b}={a*b}"); print(f"{a}/{b}={a/b}")
print(f"{a}%{b}={a%b}")
#Comparison
print(f"{a}=={b}:{a==b}"); print(f"{a}!={b}:{a!=b}")
print(f"{a}>{b}:{a==b}"); print(f"{a}<{b}:{a<b}")
print(f"{a}>={b}:{a>=b}"); print(f"{a}<={b}:{a<=b}")

#Logical
t,f=True,False
print(f"t and f:{t and f}"); print(f"t or f:{t or f}")
print(f"not f:{not f}")

#Bitwise
m,n=5,3
print(f"{m}&{n} : {m&m}" ); print()



