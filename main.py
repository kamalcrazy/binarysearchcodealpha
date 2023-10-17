start = int(input(" starting value: "))
max_range = int(input(" maximum range: "))
if max_range < start:
    print("Max_range should be greater than or equal to the starting value.")
else:
    print(f"Range of numbers with a difference of two from {start} to {max_range}:")
    for num in range(start, max_range + 1, 2):
        print(num)
