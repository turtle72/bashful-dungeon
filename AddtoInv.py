
def addtoInv(t,i):
    if type(t) == list:
        if not t:
            t.append(i)
        if i not in t:
            print(i)
            t.append(i)
    if type(t) == str or type(t) == int or type(t) == bool:
        if i != t:
            t=i
            return(t)