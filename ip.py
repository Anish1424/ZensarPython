# user_var1=int(input("Enter IPV4 adresses of Byte 1: "))
# binary_val1=bin(user_var1)[2:]
# user_var2=int(input("Enter IPV4 adresses of Byte 2: "))
# binary_val2=bin(user_var2)[2:]
# user_var3=int(input("Enter IPV4 adresses of Byte 3: "))
# binary_val3=bin(user_var3)[2:]
# user_var4=int(input("Enter IPV4 adresses of Byte 4: "))
# binary_val4=bin(user_var4)[2:]

# final_bin_value=binary_val1 + binary_val2 + binary_val3 + binary_val4 
#print(f"IPV4 address is {user_var1}.{user_var2}.{user_var3}.{user_var4}")

# user_var1=int(input("Enter IPV4 adresses of Byte 1: "))
# user_var2=int(input("Enter IPV4 adresses of Byte 2: "))
# user_var3=int(input("Enter IPV4 adresses of Byte 3: "))
# user_var4=int(input("Enter IPV4 adresses of Byte 4: "))
# print(f"IPV4 address is {user_var1}.{user_var2}.{user_var3}.{user_var4}")


# sub_net_mask=255255255128


#Task 2  /*
"""  uservar = 192
uservar1 = 168
uservar2 = 1
uservar3 = int(input("ENTER LAST OCTET OF IPV4 ADDRESS : "))

print(f"IPV4 ADDRESS is: {uservar}.{uservar1}.{uservar2}.{uservar3}")

# Network address 
net_use = uservar & 255
net_use1 = uservar1 & 255
net_use2 = uservar2 & 255
net_use3 = 0 
print(f"Network address is {net_use}.{net_use1}.{net_use2}.{net_use3}")

# Broadcast address
bro_use = uservar | 0
bro_use1 = uservar1 | 0
bro_use2 = uservar2 | 0
bro_use3 = 255 
print(f"Broadcast address is {bro_use}.{bro_use1}.{bro_use2}.{bro_use3}")

# Usable IP range
print(f"Usable range is {net_use}.{net_use1}.{net_use2}.1 to {bro_use}.{bro_use1}.{bro_use2}.{bro_use3 - 1}")
"""

#Control Statement in Python:
#if-elif-else 
'''
num=12
if num>0:
    print(f"number {num} is positive")
elif num<0:
    print(f"number {num} is negative")
else:
    print(f"number {num} is zero or not valid input")

#for loop
for i in range(1,5):
    print(i)
for i in range(5,1,-1):
    print(i)

#while
count=5
while count>0:
    print(count)
    #count=count+1
    count-=1

#Break
for i in range(1,10):
    if i==5:
        print("Break Apply at ",i)
        break
    print(f"Loop iterate : {i}")

#continue
for i in range(1,10):
    if i%2==0:
        continue #skip even num
    print(i)

#pass
for i in range(1,5):
    pass

'''    

#Functions
def greet():
    print("Hello")
greet() #function call

#Modules
import calendar as cal
print("----Calendar Program in Python----\n")
print("Enter 'x' for exit.")
y=input('Enter Year:')
if y== 'x':
    exit()
else:
    m=input("Enter month:")
    yy=int(y)
    mm=int(m)
    print("\n",cal.month(yy,mm))
