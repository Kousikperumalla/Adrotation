def changeAds(base10):
    # Write your code here
    a=bin(base10).replace("0b", "")
    s=''
    for i in a:
        if(i=='0'):
            s+='1'
        else:
            s+='0'
    return int(s,2)
