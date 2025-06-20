def total_length(sequence):
    return sum(len(s) for s in sequence)


strings = ["apple", "banana", "cherry", "date"]

total = total_length(strings)

print(f"Сумма длин всех строк: {total}")
