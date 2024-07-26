def closest50(n):
    return abs(n-50)

thislist=[100,50,65,82,23]
thislist.sort(key = closest50)
print(thislist)