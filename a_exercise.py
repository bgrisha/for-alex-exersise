a=input("enter roman number please ")
def value(a):
    if (a == 'I'):
        return 1
    if (a == 'V'):
        return 5
    if (a == 'X'):
        return 10
    
    return -1
print(value(a))    