#1.(i)write the following in both camel and snake case
#snake case
#a)student_marks
#b)total_average_mark

#camel case
#studentMarks
#totalAverageMark

#ii)age=20 into float, its new data type
age = 20
new_age =float(age)
print((new_age),type(new_age))

#3.(i)student_marks=[78,83,90,88,75], sum item 
student_marks=[78,83,90,88,75]
sum_no = 78 + 83 + 90 + 88 + 75
print(f"The sum of the items in the student_marks list is " +str (sum_no))

#(ii)display first and last items in the list
first_item = student_marks[0]
last_item = student_marks[-1]
print(f"{first_item} , {last_item}")

#(iii)add 96 to the list
student_marks.append(96)
print(student_marks)

#(iv)update 78 to 87
student_marks[0] = 87
print(f"The updated marks " +str(student_marks))

#2.(ii)write a program that asks the user to input 3 numbers,
# and find the minimum number, test your program 
# by entering the 3 different numbers. 
num1 = float(input("Enter the first_no.."))
num2 = float(input("Enter the second_no.."))
num3 = float(input("Enter the third_no.."))

min_no = min(num1,num2,num3)
print(f" The smallest number is "+ str(min_no))

#(i)Create a function to find the  average of two numbers,
# the arguments of the function are,(x,y).
# testthe program with any two numbers of ur choice

# Function to find the average of two numbers
def find_average(x, y):
    average = (x + y) / 2
    return average

# Test the function with two numbers
num1 = 10
num2 = 20

# Call the function and display the result
average_result = find_average(num1, num2)
print(f"The average of {num1} and {num2} is: {average_result}")


