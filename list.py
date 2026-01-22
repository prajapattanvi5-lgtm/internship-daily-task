#create a list
fruits = ["apple","mango","banana","grapes","kiwi","watermelon"]

#print a list
print(fruits)

#return the number of items in list
print(len(fruits))

#list constructor
list1 = list((1,2,3))
print(list1)

#access list items
#by index
print(fruits[1])

#negative indexing
print(fruits[-2])

#using range()
print(fruits[1:5])
print(fruits[:4])
print(fruits[2:])

#negative
print(fruits[-2:-1])
print(fruits[-3:])
print(fruits[:-5])

#change list items
#using insert() -> insert the item at specified index
fruits.insert(1,"cherry")
print(fruits)

#using append() -> add the item at the end of the list
fruits.append("orange")
print(fruits)

#using extend() -> add elements from another list to current list.Add any iterables(set,tuple,dictionary etc)
color = ("red","yellow","green")
fruits.extend(color)
print(fruits)

#remove list items
#using remove()
fruits.remove("banana")
print(fruits)

#using pop() with specified index
fruits.pop(2)
print(fruits)

#pop() without index will remove the last item in the list
fruits.pop()
print(fruits)

#using clear()
#clear() -> empties the list but the list still remains without any content
fruits.clear()
print(fruits)

#using del keyword -> removes the specified index
del fruits[2]
print(fruits)


#del keyword also delete the list completely if you not give any specific index
del fruits

#loop lists
#for loop
color = ["red","yellow","green","blue"]
for x in color:
    print(x)

#using range() and len()
for i in range(len(color)):
    print(color[i])

#using while loop
i=0
while i<len(color):
    print(color[i])
    i+=1

#short hand for loop
[print(x) for x in color]

#list comprehension -> when you want to create a new list based on the values of existing list
#without comprehension
newcolor = []
for x in color:
    if "l" in x:
        newcolor.append(x)
print(newcolor)

#using list comprehension
newcolor = [x for x in color if "l" in x]
print(newcolor)

