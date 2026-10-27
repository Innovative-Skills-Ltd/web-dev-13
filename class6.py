#list 

# numbers = [10,20,30,50,25]

# mixed= ["asif", 24, 4.4, True, "Dhaka", False]

# print(mixed)
# print(mixed[4])
# print(mixed[0])
# print(mixed[-2])


# Slicing (start, stop-1)

mixed= ["asif", 24, 4.4, True, "Dhaka", False]
# print(mixed)
# print(mixed[1:4])

#          0, 1,  2,  3,  4,  5,  6,  7,  8
# numbers = [1, 10, 20, 30, 40 ,50 ,60, 70, 80]

# print(numbers[:])

# # step
# print(numbers[1:8:2])

# append, insert, extend
# numbers = [1, 10, 20, 30]
# print(numbers)

# numbers.append(80) # value add in last
# print(numbers)

# numbers.insert(2, 22)
# print(numbers)

mixed= ["asif", 24, 4.4, True, "Dhaka", False]
# print(mixed)
# mixed.insert(-1, "alamin")
# print(mixed)

mixed= ["asif", 24, 4.4]
# print(mixed)

# mixed2= ["Dhaka", False]

# mixed.extend(mixed2)
# print(mixed)

# mixed2.extend(mixed)
# print(mixed2)


# remove 
mixed= ["asif", 22, 4.4]
# mixed.remove(22)
# print(mixed)

#pop()
mixed= ["asif", 22, 4.4]
# mixed.pop()

# mixed.pop(1)
# mixed.clear()

# del 
# del mixed[2]
# print(mixed)



numbers = [1, 100, 20, 30, 20, 30, 20, 30, 20, 30, 20, 30, 20, 30, 20, 30, 20, 30, 20, 30, 20, 30, 20, 30, 20, 30, 20, 30, 20, 30, 20, 30]
# print(numbers)
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# numbers.sort()
# numbers.sort(reverse=True)
# numbers.reverse()

# print(numbers)


# tuple
mixed_t= ("asif", 24, 4.4, True, "Dhaka", False)

# Set - Unique and order kore thake na 
mixed_s= {"asif", 24, 4.4, True, "Dhaka", False, "asif", False}
# print(mixed_s)

numbers_2 = [1, 100, 20, 30, 100, 20]
# print(numbers_2)
num_set= set(numbers_2)
# print(num_set)
           
           
           
a = {1, 2, 3, 4}
b= {3,8,9}
#union
# print(a | b)

# print( a & b)

# print(a - b)
# print(a.difference(b))
# print(b - a )

print(a ^ b)
print(a.symmetric_difference(b))

# next class - subset, superset, disjoint, dictionary, loop


# lower - 