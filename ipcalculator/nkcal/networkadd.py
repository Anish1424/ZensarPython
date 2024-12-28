def networkadd(uservar,uservar1,uservar2,uservar3):
    net_use=uservar&255
    net_use1=uservar1&255   
    net_use2=uservar2&255
    net_use3=uservar3&0
    print(f"network address is {net_use}.{net_use1}.{net_use2}.{net_use3}")