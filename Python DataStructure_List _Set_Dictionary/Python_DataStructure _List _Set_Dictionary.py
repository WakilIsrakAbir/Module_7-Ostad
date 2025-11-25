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

for index,x in enumerate(items):
    print(index,x,items[index])

print()

items=[1,2,3]
another_list=[4,5,6]
items.append(another_list)
print(items)
print("The list has {} items.".format(len(items)))
print(items[3][2])

items=[1,2,3]
print(dir(items))
print(help(list.sort))

s=[4,6,7,1,3,9]
s.sort()
print(s)
s.sort(reverse=True)
print(s)

m=[1,5,8]
m[0]=9
print(m)

t=(1,2,3,2,2,3)
print(t,type(t))
# print(dir(t))
print(t.count(2))
print(t.index(3))

swap
a=10
b=5
temp=b
b=a
a=temp
b,a=a,b
print(a,b)


#Set
s={1,2,3,4,5,6}
s.add(4)
s.add(8)
print(s,type(s))

li=[1,2,3,4]
s=set(li)
print(s,type(s))

li=[1,2,3,4,5,5]
s=set(li)
li=list(s)
print(li,type(li))

s={1,2,3}
print(3 in s)


text=" blue calms like a quiet sea, red ignites like a beating heart, green breathes like a forest after rain. red green blue"
colors=["red","green","blue","white"]
li=[]
word_list=text.split()
for word in word_list:
    if word in colors:
        li.append(word)
print(li)

text=" blue calms like a quiet sea, red ignites like a beating heart, green breathes like a forest after rain. red green blue"
colors=["red","green","blue","white"]
li=set()
word_list=text.split()
for word in word_list:
    if word in colors:
        li.add(word)
print(li)


#Dictionary
text=" blue calms like a quiet sea , red ignites like a beating heart , green breathes like a forest after rain. red green blue"
colors=["red","green","blue","white","heart","sea"]
dt={}
word_list=text.split()
for word in word_list:
    if word in colors:
        if word not in dt.keys():
            dt[word]=1
        else:
            dt[word] +=1
print(dt)
