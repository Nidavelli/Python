def closeto(n):
    return abs(n-50);

thislist=[100,50,65,82,23,42,36,78,62]
thislist.sort(key = closeto)
print(thislist)