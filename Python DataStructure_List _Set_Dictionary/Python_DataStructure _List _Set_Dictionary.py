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

print()

for i, item in enumerate(items):
    print(i,item)

print()

li2=[4,5,6,7]
items=items+li2
#items.extend(li2)
#items.append(li2)
print(items)

