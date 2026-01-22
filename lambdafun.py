#lambda with filter()
#The filter() function creates a list of items for which a function returns True
numbers = [11,20,15,13,16,14,30]
even = list(filter(lambda x: x % 2 == 0,numbers))
print("Even numbers are:",even)

#lambda function with map()
#map() function applies a function to every item in an iterable
numbers = [1,2,3,4,5]
double = list(map(lambda x: x*2 , numbers))
print(double)

#lambda with sort()
#The sorted() function can use a lambda as a key for custom sorting
names = ["tanvi","ankit","ansh","nandita","anshita"]
sorted = sorted(names, key=lambda x: len(x))
print(sorted)

