from binary_search_tree import BinarySearchTree
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# optimized O(log n)
bst = BinarySearchTree(names_1[0])
for name in range(1, len(names_1)):
  bst.insert(names_1[name])
# print(bst.contains('Ronnie Barrera'))
print(bst.contains('Hallie Vazquez'))

duplicates = []
for name2 in names_2:
  if bst.contains(str(name2)):
    duplicates.append(name2)

    

# runtime O(n^2)
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
