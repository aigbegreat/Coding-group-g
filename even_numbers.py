def even_numbers(start, stop, loop=1):
    if start % 2:
        start += 1
    while loop:
        for i in range(start, stop + 1, 2):
            yield i
        loop = loop - 1 if loop >= 1 else loop


e = even_numbers(4, 30)
evens = [n for n in e]
print(evens)
Result:[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]