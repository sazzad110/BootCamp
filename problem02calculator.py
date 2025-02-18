def calculator(num1,num2,operator):
    res = 0
    if operator == "+":
        res = num1 + num2
    elif operator == "-":
        res = num1 - num2
    elif operator == "*":
        res = num1*num2
    else:
        if num2 == 0:
            raise ZeroDivisionError("Can't divide by zero !!!")
        
        res = num1/num2

    return res
    
    
if __name__ == "__main__":

    try:
        num1 = 10
        num2 = 0
        operator = "*"

        result = calculator(num1,num2,operator)
        print(f"The result is {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

