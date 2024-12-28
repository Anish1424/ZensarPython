import calendar as cal
def year():
    i=1
    y=input("Enter year:");
    while i<=12:
        yy=int(y);
        mm=int(i);
        print("\n",cal.month(yy,mm))
        i=i+1;
    exit();