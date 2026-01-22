#count the elements of list without using len()
list = [10,20,30,40,50]
#using for loop
count = 0
for x in list:
    count+=1
print("Total elements:",count)

#while loop
i=0
count=0
while i<len(list):
    count+=1
    i+=1
print("Total items:",count)

#print the list elements along with its index
fruits = ["apple","mango","orange","banana","pineapple"]

for i in range(len(fruits)):
    print(i,":",fruits[i])

#to calculate sum of list elements
numbers = [10,20,30,40,50]
sum = 0

for i in numbers:
    sum += i
print("Sum of elements are:",sum)

#print total odd and even numbers in a list
numbers = [1,2,3,5,6,4,8,9]
even = 0
odd = 0

for i in numbers:
    if i%2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:",even)
print("Odd numbers:",odd)


