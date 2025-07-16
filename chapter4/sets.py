# set is the collection of unordedred - each elemnet in the sets  must be unique and immutable
# sets are mutable but in the elements in sets are immutable -- we pass the tuple in sets but not t he list and dictionary

# set = {1,2,2,4,4, "world", "hello", "world"}
# collection = set()

# print(type(set))
# print(set) #ignore the duplicate items in sets

# methods in sets


# collection = set()

# collection.add(1)
# collection.add(2)
# collection.add("python")
# collection.add((1,2,3))
# collection.add([1,2,3]) #hashing is the algorithm in which we convert the original value into anyother value --unhashable type: 'list', dictionary and sets


# collection.remove(9)
# print(len(collection))
# collection.clear()
# print(len(collection))

# collect = {"hello", "aqsa", "city", "college", "working", "lerarning"}

# print(collect.pop())
# print(collect.pop())

# print(collect)

set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2)) #return the new set the original set remians the same values
print(set1.intersection(set2))
