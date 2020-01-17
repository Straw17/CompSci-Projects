#This is a program by Evan Conway that solves quadratic equations
import math

def quadForm(a, b, c): #this takes the necessary info and returns the result
    try:
        x =(-b + math.sqrt(b**2-(4*a*c)))/(2*a) #try the formula
    except (ValueError, ZeroDivisionError) as e:
        x = 'NO SOLUTION FOUND' #if there is no solution, set x to a string with info
    return x

while True: #loop the whole program
    while True: #get inputs as int
        try:
            a = int(input('Enter the coefficient of the first element: '))
            b = int(input('Enter the coefficient of the second element: '))
            c = int(input('Enter the third element: '))
            break
        except ValueError:
            continue
    print(quadForm(a, b, c)) #print result
    if input('Run again?\n').lower() == 'no': #end loop if user wants to
        break
