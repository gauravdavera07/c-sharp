nm={"snm":"stud1","roll1":"1"}
print(nm)
x=nm.get("snm")
print(x)
y=nm.get ("roll1")
print(y)

x=nm.keys()
print(x)
y=nm.values()
print(y)
a=nm.items()
print(a)

nm["snm"]="stud2"
print(nm)
nm.update({"roll":"3"})
print(nm)
nm.pop("roll")
print(nm)
nm.popitem()
print(nm)