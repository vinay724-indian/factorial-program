def calculate_factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

# Hardcoded value for automated Jenkins execution
num = 5 
print(f"The factorial of {num} is {calculate_factorial(num)}")