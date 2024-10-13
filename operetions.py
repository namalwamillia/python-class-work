#1.) write the program that takes two numbers as input and displays their sum, difference , their product and quationt
#let numbers be num1 and num2
# this step we input the nums
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#this step we make calculations on numbers to  be input above
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
modulus = num1 % num2
floor_division = num1 // num2

#Display the results of the input numbers
print(f"The Sum of num1 and num2: {sum_result}")
print(f"The Difference of num1 and num2: {difference}")
print(f"The Product of num1 and num2: {product}")
print(f"The Quotient  of num1 and num2: {quotient}")
print(f"The Modulus  of num1 and num2: {modulus}")
print(f"The floor division  of num1 and num2: {floor_division}")




# 2.)Write a program that compares two integers and prints whether the first number is greater than, less than or equal to the 2nd number

#let the 2 numbers be num1 and num2
num1 = 2
num2 = 2
if num1 > num2:
    print("num1 is greater than num2")
elif num1 < num2:
    print("num1 is less than num2")
else:
    print("they are equal")
   

#3.) Write a program which checks if a given number is btn 10 and 20 ( where 20 inclusive) using logical operaters


def is_between_10_and_20(number):
    return number > 10 and number <= 20  # Logical operators used here

# Test the function
num = int(input("Enter a number: "))
if is_between_10_and_20(num):
    print(f"{num} is between 10 and 20 (exclusive of 10, inclusive of 20).")
else:
    print(f"{num} is not between 10 and 20 (exclusive of 10, inclusive of 20).")


# 4.)Write a program that prints the squares of integers from one to 10 using a for loop
# Loop through integers from 1 to 10
# Loop through integers from 1 to 10
for number in range(1, 11):
    square = number ** 2
    print(f"The square of {number} is {square}")

