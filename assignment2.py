#Assignment two
#qn.1)  # The volume of a sphere with radius r is (4/3)* pie * r**2. 
# What is the volume of the sphere with radius 5. 
# Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places
    
    
# we have to read the value of pi
pi = 3.14159

# Get radius input from the user
radius = float(input("Enter the radius of the sphere: "))

# Calculate the volume of the sphere
volume_of_sphere = (4/3) * pi * (radius ** 2)

# printing the volume_of_sphere rounded to 2 decimal places
print(f"The volume of the sphere is: {volume_of_sphere:.2f}")



#qn.2) # Create a program to calculate the area of a triangle (1/2 * base * height). 
# Base and height should be entered using the keyboard. 

# Get base and height input from the user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Here we calc the area of the triangle
area = 0.5 * base * height

# printing the area of the triangle
print(f"The area of the triangle is: {area}")



#qn.3) WITI has tasked you to automate a simple grading system. 
# As a python student, write a program using  to display the grades that 
# the students will be receiving based on the mark scored in a subject. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89%   Grade is  B
# 70% - 79%   Grade is C                                                        
# 60% - 69%   Grade is D                  
# 50% - 59%   Grade is E  
# < 50% Fail 

# define a function get_grade()
def get_grade(mark):
#Get the student grade based on the given mark.
  if mark >= 90:
    return 'A'
  elif mark >= 80:
    return 'B'
  elif mark >= 70:
    return 'C'
  elif mark >= 60:
    return 'D'
  elif mark >= 50:
    return 'E'
  else:
    return 'Fail'

# Get the student's mark
mark = float(input("Enter the student's mark: "))

# Get the grade
grade = get_grade(mark)

# Display the grade
print("The student's grade is:", grade)

#qn.4)  WITI Academy is proposing a Sacco to help students save their money. 
#  Design a platform that will do the following.
#  Welcome to, WITIAcademy Sacco.
#  1. Deposit Money
#  2. Withdraw Money
#  3. Check Balance
#  Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#  If the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
#  If the student selects 3, the account balance should be displayed.


balance = 0  # Initial balance

def deposit_money():
    global balance
    amount = float(input("Enter the amount to deposit: "))
    if amount >= 1000:
        balance += amount
        print(f"Deposit successful! Your new balance is: {balance}")
    else:
        print("The minimum deposit amount is 1000.")

def withdraw_money():
    global balance
    amount = float(input("Enter the amount to withdraw: "))
    if amount >= 500:
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful! Your new balance is: {balance}")
        else:
            print("Insufficient balance!")
    else:
        print("The minimum withdrawal amount is 500.")

def check_balance():
    print(f"Your current balance is: {balance}")

# Main program
print("Welcome to WITI Academy Sacco!")

while True:
    print("\nPlease choose an option:")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        deposit_money()
    elif choice == '2':
        withdraw_money()
    elif choice == '3':
        check_balance()
    elif choice == '4':
        print("Thank you for using WITI Academy Sacco. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
