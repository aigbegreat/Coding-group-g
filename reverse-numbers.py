def reverse_number(number):
    reversed_number = 0
    is_negative = False

    if number < 0:
        is_negative = True
        number = abs(number)

    while number != 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    if is_negative:
        reversed_number = -reversed_number

    return reversed_number

# Example usage
number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)

