# Calculate the multiplication and sum of two numbers

# pseuducode

# Define the function of multiplication and sum of two numbers
def Multiplication_or_Sum(num1, num2):

# Multiply the two numbers
    product=num1*num2
    
# Check if the product is less than 1000
    if product<=1000:
        return product
    else:
# Calculate the sum of two numbers if the product is greater than 1000
        return num1+num2
    
# Print the result of the first condition
result=Multiplication_or_Sum(20, 30)
print ("The result is", result)
