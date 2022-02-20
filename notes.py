# python has some different data types

# List
list = [1,2,3,4,5]

    # list is indexable

print(list[0])
    # // 1

    # list can pop(), extend(), append(), clear(), copy(), reverse(), etc
    # can reassign new values to list, because it is mutable
list[3] = 100

print(list)
    # // [1, 2, 3, 100, 5]

# Tuple
tuple = ('bats', 'dogs', 'cats', 'beer', 'fish', 'mirrors')

    # tuple is immutable
    # available methods are .count() and .index(x)

    # can't change values
    # can reference values however
print(tuple[0])
    # // bats

    # can't reassign values to specific indexes
    #tuple is faster than list, and requires less memory

# Set 
set = {4,6,4,23,4,6,53,23,643,13,44}

    # set is the fastest, and requires least memory of all
    # can't access specific index value

print(set)
    # // {643, 4, 53, 6, 23, 44, 13}
    # returns values in random order
    # can't keep duplicate values in a set, will only store unique values
    # set can use methods like add(), clear(), delete(), pop(), update() and a bunch more. 
    # its really fast to use, but returns values in random order, so less easy to access specific values

