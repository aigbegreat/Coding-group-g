lower_values =int(input("please, enter the lowest Range number:"))
upper_values = int(input("please,enter the higher Range number:"))
print ("The Prime Numbers in the range are: ")
for number in range (lower_values, upper_values + 1):
    if number > 1:
        for i in range (2, number):
            if (number % i) == 0:
                break
        else:
            print (number)