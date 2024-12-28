import calendar as cal
def month():
    print("Enter X for exit.");
    y=input("Enter year:");
    if y=='X':
        exit();
    else:
        m=input("Enter Month:")
        yy=int(y);
        mm=int(m);
        print("\n",cal.month(yy,mm))