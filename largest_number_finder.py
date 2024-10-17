# Input 5 numbers
num1 = int(input("Please Enter the First Number: "))
num2 = int(input("Please Enter the Second Number: "))
num3 = int(input("Please Enter the Third Number: "))
num4 = int(input("Please Enter the Fourth Number: "))
num5 = int(input("Please Enter the Fifth Number: "))

# Comparing num1 to other variables
if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
    print(f"The Largest Number: {num1}")
# Comparing num2 to other variables
elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
    print(f"The Largest Number: {num2}")
# Comparing num3 to other variables
elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
    print(f"The Largest Number: {num3}")
# Comparing num4 to other variables
elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
    print(f"The Largest Number: {num4}")
# If none of the conditions are true, num5 is the largest
else:
    print(f"The Largest Number: {num5}")

