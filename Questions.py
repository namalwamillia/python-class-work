# address = input("Enter your address: ")
# age =  (input("Enter your age: ")) 

# print(f"Address: {address} (Type: {type(address)})")
# print(f"Age: {age} (Type: {type(age)})")


#Assignment one

 # write a simple program that asks the user for their age, if the age is greater or equal to 18,
# print  your an adult and qualified, else you are not qualified.

user_age = int(input("Enter your Age: "))

if user_age >= 18:
    print("You are an Adult and qualified") #112999
    
else:
    print("You are not Qualified")
    
    
# qn1)we have the following student details and marks.enter this details from the keyboard.: Student_name=Ritah,
 #Student_no = SEP23/bcs/14,programming = 78,Data science =89,computer_application_marks = 55 calculate the averege mark and 
# print the results in three decimal places

student_name = str(input("Enter your name: "))
student_no = str(input("Enter your Reg.no: "))
computer_application_marks =int(input("Enter your computer_application_marks"))
Programming_marks = int(input("Enter your programming marks: "))
data_science_marks= int(input("Enter your Data Science marks: "))

number_of_course_units = 3
total_marks = Programming_marks + data_science_marks + computer_application_marks
print(f"total_marks is:{total_marks}")
average_marks = total_marks / number_of_course_units

print(f"The average_marks is:{average_marks:.3f}")

# qn2)write a program that converts Celsius temp to Fahrenheit. the program should ask the user to enter the temp in Celsius degress and
# then displays the temp convertd to Fahrenheit degree

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#  temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))

# temperature to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# result
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")


#3)a cars mile par gallon can be calculated by this formula, mpg = milesdriven/gallons of gas used
# write a program that asks the user to calculate the cars miles par gallon and display the formula

# Ask the user for input

miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the number of gallons of gas used: "))

# Calculate miles per gallon (MPG)
if gallons_used != 0:
    mpg = miles_driven / gallons_used
    # Display the result
    print(f"The car's miles per gallon (MPG) is: {mpg:.2f}")
else:
    print("Gallons used cannot be zero. Please enter a valid number.")
    
    
    #Assignment two
#qn.1)  # The volume of a sphere with radius r is (4/3)* pie * r**2. 
# What is the volume of the sphere with radius 5. 
# Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places
    
#qn.2) # Create a program to calculate the area of a triangle (1/2 * base * height). 
# Base and height should be entered using the keyboard. 

#qn.3)#Question One
# WITI has tasked you to automate a simple grading system. 
# As a python student, write a program using  to display the grades that 
# the students will be receiving based on the mark scored in a subject. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89%   Grade is  B
# 70% - 79%   Grade is C                                                        
# 60% - 69%   Grade is D                  
# 50% - 59%   Grade is E  
# < 50% Fail 

#qn.4) #  WITI Academy is proposing a Sacco to help students save their money. 
#  Design a platform that will do the following.
#  Welcome to, WITIAcademy Sacco.
#  1. Deposit Money
#  2. Withdraw Money
#  3. Check Balance
#  Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#  If the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
#  If the student selects 3, the account balance should be displayed.
