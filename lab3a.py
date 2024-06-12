#!/usr/bin/env python3

# return_text_value() function

# Author ID: 119911220

def return_text_value():
    # This function returns a greeting message as a string
    name = 'Terry'
    greeting = 'Good Morning ' + name 
    return greeting

# return_number_value() function

def return_number_value():
    # This function returns the sum of two integers
    num1 = 10
    num2 = 5
    return num1 + num2



# Main Program

if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))