# Name: Luke Bowden
# Student Number: t00040951
# Lab Number: 3
# Date: 2020-10-02
# Description: Generates a random password for the user.

# Importing the random package
import random

#Declaring Constant variables
MIN_PASS_LENGTH = 7;
MAX_PASS_LENGTH = 10;
MIN_RAND_INT = 33;
MAX_RAND_INT = 126;

#Function to generate random password
def randomPassword():
    #Creates an empty Password String and declares an index variable
    password = '';
    i = 0;
    
    #Deciding the length of the password between 7 and 10
    length = random.randint(MIN_PASS_LENGTH, MAX_PASS_LENGTH);
    
    #While loop that runs until the index hits the randomly selected pass length 
    while(i < length):
        
        #Gets a random int between and including 22 and 126
        rand = random.randint(MIN_RAND_INT, MAX_RAND_INT);
        
        #Converts the randomly generated number into a char on the ASCII table
        result = chr(rand);
        
        #Appends the char to the empty password string
        password += str(result);
        
        #Increases the index
        i += 1;
    
    #When the loop breaks it prints your newly generated random password
    print("Your random password is: " + password);    

#Main function to execute the randomPassword() function
def main():
    randomPassword()
        

#Executes the main function
if __name__ == "__main__":
    main()
    