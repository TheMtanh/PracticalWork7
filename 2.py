def extract_positive(numbers):
    return [num for num in numbers if num > 0]


numbers = [-5, 3, -2, 8, 0, -1, 4, -7, 6]

positive_nums = extract_positive(numbers)

print("Положительные числа:", positive_nums)