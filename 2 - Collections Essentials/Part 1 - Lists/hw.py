# Problem 1
def remove_duplicates(items):
    duplicate_items = []
    for item in items:
        if item not in duplicate_items:
            duplicate_items.append(item)
    return duplicate_items

print(remove_duplicates([1, 2, 2, 3, 1, 4])) # [1, 2, 3, 4]
print(remove_duplicates(["a","b","a","c"])) # ['a','b','c']
print(remove_duplicates([5, 5, 5])) # [5]
print(remove_duplicates([])) # []

# Problem 2
def find_common(list1, list2):
    common_items = []
    for item in list1:
        if item in list2 and item not in common_items:
            common_items.append(item)
    return common_items

print(find_common([1, 2, 3], [2, 3, 4])) # [2, 3]
print(find_common(["a","b"], ["c","d"])) # []
print(find_common([1, 1, 2], [2, 2, 3])) # [2]
print(find_common([], [1, 2])) # []

# Problem 3
def reverse_sublists(data, size):
    reversed_data = []
    for i in range(0, len(data), size):
        sublist = data[i:i+size]
        reversed_data.extend(reversed(sublist))
    return reversed_data

print(reverse_sublists([1, 2, 3, 4, 5, 6], 2)) # [2, 1, 4, 3, 6, 5]
print(reverse_sublists([1, 2, 3, 4, 5], 3)) # [3, 2, 1, 5, 4]
print(reverse_sublists([1, 2, 3, 4], 1)) # [1, 2, 3, 4]
print(reverse_sublists([1, 2, 3], 5)) # [3, 2, 1]

#Problem 4
def rotate_list (items, positions):
    positions = positions % len(items) if items else 0
    return items[-positions:] + items[:-positions]

print(rotate_list([1, 2, 3, 4, 5],-2)) # [3, 4, 5, 1, 2]
print(rotate_list([1, 2, 3, 4, 5], 2)) # [4, 5, 1, 2, 3]
print(rotate_list([1, 2, 3], 0)) # [1, 2, 3]
print(rotate_list([1, 2, 3], 5)) # [2, 3, 1]