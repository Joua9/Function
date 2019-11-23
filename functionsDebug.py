'''
Created on Sep 24, 2019

@author: amayamunoz
'''

'''
For this assignment you should look at the functions created below and find the error.
For each task, there will be one error that you must find and correct.
Sometimes there will be an explanation of the problem and/or tips that can help you
complete the tasks.
EXAMPLE TASK:
'''
#EX)
# This function should take in three numbers and add them together
# Does not do desired function:
# def multiply_three_numbers(num1, num2) :
#    sumOfThreeNumbers = num1 * num2
#    return sumOfThreeNumbers
# Correct:
def multiply_three_numbers(num1, num2, num3):
    sumOfThreeNumbers = num1 + num2 + num3
    return sumOfThreeNumbers
'''
END EXAMPLE
'''

#1)
# This function should take in three numbers and multiply them together
# Does not do desired function:
# def multiply_three_numbers(num1, num2): 
#    productOfThreeNumbers = num1 * num2
#    return productOfThreeNumbers
# Correct:
def multipling_three_numbers (num1,num2,num3):
    productOfThreeNumbers = num1 * num2 *num3
    return productOfThreeNumbers
productOfThreeNumbers =multiply_three_numbers(1,2,3)
print(productOfThreeNumbers)

#2) 
# This function has the wrong naming conventions:
# def Multiply by Two(num1):
#    multiplied = num1 * 2
#    return multiplied
# Correct:
def multiply_two_numbers(num1,num2):
    productOfTwoNumbers=num1*num2 
    return productOfTwoNumbers

productOfTwoNumbers=multiply_two_numbers(1,2)
print(productOfTwoNumbers)
#3) 
# This function uses one more line than necessary, make it do the same function
# but in one line
# def divide_by_ten(num):
#    divided = num / 10
#    return divided
def divide_by_ten(num1): 
    divideByTen= num1/10
    return divideByTen
divideByTen=divide_by_ten(20)
print(divideByTen)