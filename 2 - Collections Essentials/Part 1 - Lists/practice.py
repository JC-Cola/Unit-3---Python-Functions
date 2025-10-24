# Question 3: Code Writing
def filter_evens(numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers

print(filter_evens([1, 2, 3, 4, 5, 6]))
print(filter_evens([10, 15, 20, 25]))
print(filter_evens([1, 3, 5]))

# Question 6: Code Writing
def list_stats(numbers):
    if(numbers):
        mini = min(numbers)
        maxi = max(numbers)
        avg = sum(numbers) / len(numbers)
        return [mini, maxi, avg]
    return None
    
print(list_stats([10, 20, 30, 40]))
print(list_stats([5, 5, 5]))
print(list_stats([]))
