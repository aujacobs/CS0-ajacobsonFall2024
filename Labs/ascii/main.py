"""
    StdIO Lab
    ASCII Art - using literals and variables
    
    Updated By: Austin Jacobson #fixed#
    Date: 8/27/24 #fixed#
    
    This program produces an ASCII art on the console.

    Algorithm steps: 
    1. Use variables to store data/values
    2. Write a series of print statements to print the data/values to the console
"""
print("Welcome to ASCII Art Program...\n")
name="Austin"
print("Nice meeting you",(name)+"!\n") 

#fixed#
#fixed#
#prompt user to enter the semester and store the value into semester variable using input function

semester=input("What semester is this?\n\n")
print("\nThis is the" , semester + " semester.\n")

#fixed#
#fixed#
#must output: This is <year> year.

year=input("What year is it?\n\n")
print("\nThis is", year + " year.\n")

print("Hope you like my ASCII art...\n\n")

line1="  |\\_/|   **********************    (\\_/)"
line2=" /@   @\\  *      ASCII Lab     *   (='.'=)"
line3="( > 0 < ) *   Austin Jacobson  *   (\")_(\")"
line4=" >> x <<  *      CSCI 110      *"
line5="/   O  \\  **********************\n"
line6="pianooo\n"
line7=" _______________________________________________"
line8="|| | | ||| | ||| | | ||| | ||| | | ||| | ||| | ||"
line9="||_|_|_|||_|_|||_|_|_|||_|_|||_|_|_|||_|_|||_|_||"
line10="| | | | | | | | | | | | | | | | | | | | | | | | |"
linefinal="|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|"

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)
print(line8)
print(line9)
print(line10)
print(linefinal)

#fixed#
#fixed#
#fixed#
#fixed#
# Note: You can add more lines or print more ASCII arts of your choice

print("\nGood bye...  \n")