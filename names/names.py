import time
from collections import Counter  

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value and self.right:
            return self.right.contains(target)
        elif target < self.value and self.left:
            return self.left.contains(target)
        return False


bst = BSTNode("M")
for i in names_1:
    bst.insert(i)

for i in names_2:
    if bst.contains(i):
        duplicates.append(i)


# names_1count = Counter(names_1)
# names_1_single = []
# for x, y in names_1count.items():
#     if y == 1:
#         names_1_single.append(x)

# names_2count = Counter(names_2)
# names_2_single = []
# for x, y in names_2count.items():
#     if y == 1:
#         names_2_single.append(x)

# database = Counter(names_1_single + names_2_single)

# for x, y in database.items():
#     if y > 1:
#         duplicates.append(x)


# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
            
# runtime complexity is On^2
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
