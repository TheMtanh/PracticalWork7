def sorted_digit(numbers):
    return sorted(num for num in numbers if 10 <= num <= 99)


numbers = [-15, 3, 25, 8, 0, -1, 45, 100, 16, 7]

two_digit_nums = sorted_digit(numbers)

print("Отсортированные числа:", two_digit_nums)