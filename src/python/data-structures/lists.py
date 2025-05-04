## Create a list

### Create an empty list

l = []
assert len(l) == 0
assert l == []
print(f"Empty list: {l}")

### Create a list with 3 elements
l = [1, 2, 3]
assert len(l) == 3
assert l == [1, 2, 3]
print(f"List with 3 elements: {l}")

### Create a list with 3 elements using a different method
l = list((1, 2, 3))
assert len(l) == 3
assert l == [1, 2, 3]
print(f"List with 3 elements: {l}")

### Create a list with 3 elements using a different method
l = list(range(1, 4))
assert len(l) == 3
assert l == [1, 2, 3]
print(f"List with 3 elements: {l}")

### Create s list using a list comprehension
l = [x for x in range(1, 4)]
assert len(l) == 3
assert l == [1, 2, 3]
print(f"List with 3 elements: {l}")

## Access elements

### Access the first element
el = l[0]
assert el == 1
print(f"First element: {el}")

### Access the last element
el = l[-1]
assert el == 3
print(f"Last element: {el}")

### Access the second element
el = l[1]
assert el == 2
print(f"Second element: {el}")

try:
    el = l[3]
except IndexError:
    print("The element doesn't exist. IndexError: list index out of range")

## Add elements

### Add an element to the end of the list
l = ["one", "two", "three"]
l.append("four")
assert len(l) == 4
assert l == ["one", "two", "three", "four"]
print(f"List with 4 elements: {l}")

### Add an element to the end of the list using the + operator
l = ["one", "two", "three"]
l = l + ["four"]
assert len(l) == 4
assert l == ["one", "two", "three", "four"]
print(f"List with 4 elements: {l}")
