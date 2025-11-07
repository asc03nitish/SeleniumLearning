def calculate_total(numbers):
    total = 0

    for num in numbers:
        total += num

    return total


def process_data(numbers):
    total = calculate_total(numbers)  # Extracted method

    average = total / len(numbers)

    return average


data = [1, 2, 3, 4, 5]

result = process_data(data)

print("Average:", result)

