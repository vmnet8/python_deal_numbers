def main():
 
     # Welcome greeting
     print('This program will do various operations based on two')
     print('   numbers that you enter. The numbers must be positive')
     print('   integers in the range of 1-1000 and cannot be the same.')
     print()
 
     # Declarations and initializations
     keepgoing = 'c'
 
     # Start the loop structure
     while keepgoing == 'c' or keepgoing == 'C':
 
         # Get user integers with input validation
         num1 = int(input("Please enter your first integer: "))
         while num1 < 0 or num1 > 1000:
             num1 = int(input('   ERROR: only enter an integer between 1-1000: '))
         num2 = int(input("Please enter your second integer: "))
         while num2 < 0 or num2 > 1000 or num2 == num1:
             num2 = int(input('   ERROR: only enter a different integer between 1-1000: '))
 
         # Various operations
         print('Added together:     ', num1, "+", num2, "=", format(addThese(num1, num2), ',d'))
         print('Multiplied together:', num1, "x", num2, "=", format(multiplyThese(num1, num2), ',d'))
         print('Sum of squares:      ', num1, '^2 + ', num2, '^2 = ', format(squareThese(num1, num2), ',d'), sep="")
         print('Sum of cubes:        ', num1, '^3 + ', num2, '^3 = ', format(cubeThese(num1, num2), ',d'), sep="")
         print('Which is bigger between ', num1, ' and ', num2, ': ', format(compareThese(num1, num2), ',d'), sep="")
 
         # Continue or not, with input validation?
         print()
         keepgoing = input("(C)ontinue or (Q)uit? ")
         while keepgoing != 'c' and keepgoing != 'C' and keepgoing != 'q' and keepgoing != 'Q':
             keepgoing = input("   ERROR: only enter (C)ontinue or (Q)uit:")
 
     # Goodbye greeting
     print()
     print('Thank you for using this program. Program ending.')
 
def addThese(a, b):
     return a + b
 
def multiplyThese(a, b):
     return a * b
 
def squareThese(a, b):
     return a * a + b * b
 
def cubeThese(a, b):
     return a * a * a + b * b * b
 
def compareThese(a, b):
     if a > b:
         return a
     else:
         return b
 
# Call the main function
main()
# add some comments  at the  end
