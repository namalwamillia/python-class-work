#Assignement Operators

sum =5
sum += 6
print(sum)

#Given that we hve two products a laptop and a mouse such that the price of a laptop 
#is 300,000.Shs and the price of a mouse is 50,000..use a for loop to find the total sum of the products
laptop = 300000
mouse = 50000
sum = 0

#for loop
product_prices =[laptop , mouse]
for price in product_prices:
    sum+= price
    print(f" The total sum of the product is {sum:,}")
    
    
# 4.)Write a program that prints the squares of integers from one to 10 using a for loop
# Loop through integers from 1 to 10

for number in range(1, 11):
    square = number ** 2
    print(f"The square of {number} is {square}")

    






