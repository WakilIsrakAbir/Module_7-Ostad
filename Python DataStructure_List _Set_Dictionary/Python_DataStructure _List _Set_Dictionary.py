items=[]
items.append(1)
items.append(2)
items.append("Hello")
items.append([10,20,30])
print(items)
print(items[-1])

print()

for i in range(0,len(items)):
    print(i,items[i])

print()

for item in items:
    print(item,type(item))
