from menu1 import m1
from menu2 import m2
def main():
    print("-------calendar program in python--------\n")
    i=''
    while i!='n':
        print("1.Specific Month")
        print("2.Specific Year")
        print("3.exit.")
        y=input("Enter choice:")
        if y=='3':
            exit()
        elif y=='1':
            m1.month()
        else:
            m2.year()
        i=input("Do you want to continue : y/n")
main()