import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"), x.hour,":",x.minute,x.strftime("%p"))
print(x.strftime("%c"))