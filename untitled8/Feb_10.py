import spytools

#reverse list by creating a new list
numbers = [10, 12, 5, 18, 3]
new_numbers = []
for i in range(len(numbers) - 1, -1, -1):
    new_numbers.append(numbers[i])
    print(new_numbers)

#reverse a list in place
for i in range(len(numbers) // 2):
    j = len(numbers) - i + 1
    numbers[i], numbers[j] = numbers[j], numbers[i]
    print(numbers)

"""
for i, number in enumerate(numbers):
    numbers[i] = number + 10
    print(numbers)
"""

s = spytools.gen_consecutive_chars()
print (s)