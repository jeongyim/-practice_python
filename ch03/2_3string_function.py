a = "Hello python"
b = "I like apple"

print(len(a))
print(a.isupper())
print(a.upper())
print(a.islower())
print(a.lower())
print(b.replace("I","You"))
c = a.lower()
print(c)
print(c.capitalize())
print(c.title())
print(a.count("l"))
print(a.startswith("He"))
print(b.endswith("ap"))
print(b.endswith("le"))

c="1233344442"
print(c.isdigit())
print(c.isalpha())
print(type(c))
d=int(c)
print(type(d))
print(c.find("2"))
add=c.index("2")
print(add)
print(c.index("2",add+1))
print(c.find("java"))
#print(c.index("java"))
print("hi")
c = "a,b,c,d,e"
print(c.split(","))