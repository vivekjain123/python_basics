
# Generators doesnt hold all the values in the memory unlike list.
# simple example using a square function
def square_nums(nums):
    for i in nums:
        yield (i * i)
        
result = square_nums([1, 2, 3, 4, 5])
# next is used to get the next value from the list
print(next(result))
print(next(result))

# same can be achieved by using list comprehension
# replace brackets with parenthesis
sqr_nums = (x * x for x in [1, 2, 3, 4])

# it will print the generator object
print(sqr_nums)

# iterate over all the values using for loop
for num in sqr_nums:
    print(num)

# convert generator to list
addTwo = (x + 2 for x in [1, 2, 3, 4])
print(addTwo)
addTwoList = list(addTwo)
print(addTwoList)
