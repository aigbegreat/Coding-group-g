def find_largest_number(numbers):
    if not numbers:
        return None  # Return None if the list is empty

    largest = numbers[0]  # Assume the first number is the largest

    for number in numbers:
        if number > largest:
            largest = number  # Update the largest number if a larger one is found

    return largest

# Example usage:
my_list = [12, 45, 67, 23, 99, 54]
result = find_largest_number(my_list)
print("The largest number is:", result)

