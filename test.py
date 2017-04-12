def double_value(d):
    l = []
    for  value in d.values():
        l.append(value * 2)
    return l
print(double_value({'int': 5, 'float': 1.3, 'string': 'zzz'}))  