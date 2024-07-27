family={
    "Child1":{
        "name":"Emily",
        "year":"2004"},
    "Child2":{
        "name":"Tobias",
        "year":"2007"},
    "Child3":{
        "name":"Linus",
        "year":"2011",
    }
}
for x,obj in family.items():
    print(x)
    for y in obj:
        print(f"{y}: {obj[y]}")
    