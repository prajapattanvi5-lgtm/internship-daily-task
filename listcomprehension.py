#Create a list of numbers from 1 to 10 using list comprehension.
number = [i for i in range(1,11)]
print(number)

#squares of numbers
square = [i*i for i in range(1,11)]
print(square)

#even numbers from 1 to 50
even = [i for i in range(1,51) if i % 2 == 0]
print(even)

#odd numbers
odd = [i for i in range(1,51) if i % 2 != 0]
print(odd)

#convert strings to uppercase
names = ["tanvi","ankit","bharat"]
upper = [x.upper() for x in names]
print(upper)

#extract positive numbers
num = [10,20,-11,13,-15]
pos = [x for x in num if x > 0]
print(pos)

#extract negative numbers
num = [10,20,-11,13,-15]
negative = [x for x in num if x < 0]
print(negative)

#remove zeroes from the list
list = [0,1,2,0,5]
non_zero = [i for i in list if i != 0]
print(non_zero)

#number divisible by 3 and 5
new_num = [x for x in range(1,101) if x % 3 == 0 and x % 5 == 0]
print(new_num)

#length of each word
words = ["python","is","very","popular"]
length = [len(w) for w in words]
print(length)