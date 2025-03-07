def is_neon_number(n):
    square = n ** 2
    digit_sum = sum(int(digit) for digit in str(square))
    return digit_sum == n

# Taking input from user
num = int(input("Enter a number: "))

# Checking and displaying result
if is_neon_number(num):
    print(f"{num} is a Neon Number!")
else:
    print(f"{num} is NOT a Neon Number.")
