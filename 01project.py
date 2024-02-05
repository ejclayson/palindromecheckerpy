
#import => is a type of keyword use to make a code available in your project or module
#re => stands for "regular expression" and it is the module used for matching text patterns.
#this is a comment
import re

#variable => it is declared so that it can be used to store a value. 
#input => is a function used for user input
userInput = input("Please enter a string of pure characters with no spaces.\nPlease make sure that it has more than one(1) character: ")

userInputLowerCase = userInput.lower();
# on this line we declared a variable named pattern and give it a value [0-9.]+ which makes it as a str or string type of variable
pattern = "[0-9.]+";
# print(type(pattern))
# print(pattern)

# on this line we declared a variable named pattern2. 
#The value that we give the variable pattern2 is regular expression function called search. 
# search returns a Match object if there is a match anywhere in the string.
# inside search the first part contains "[a-z]+" which stands for all alphabet or from a-z therefore search will check if there are alphabet from a-z on the string that we will supply on the second part of the search()
# the second part inside the search() is the userInput variable that contains the input() function and whatever the user input to that variable will then be checked by search() if there are any alphabets from a-z on that variable.
pattern2 = re.search("[a-z]+", userInputLowerCase);
# print(type(pattern2))
# print(pattern2)

# if statement a condition statement used to check a condition. if the conditition is true then it will allow a block of code to get executed but if the condition is false then it will skip the execution of the block of code and will then proceed with either "else if" or "else" statement
#this if condition then check if the userInput variable doesn't contain anything by checking the length of userInput by using len() function so if the length of userInput is not equals or "!=" to zero then it will execute the block of code 
#in case this if condition is false then it will skip the block of code to get executed and will proceed to the "else" statement partnered with this if condition
if len(userInputLowerCase) != 0:
    #this if condition checks if the userInput variable doesn't contain anything by checking the length of userInput by using len() function
    #in case this if condition is false then it will skip the block of code to get executed and will proceed to the "else" statement partnered with this if condition
    if not userInputLowerCase.__contains__("\\s") and not userInput.__contains__(" ")  and not userInput.__contains__("\t"):
        if userInputLowerCase != pattern:
            if len(userInputLowerCase) > 1:
                if pattern2 :

                    z = len(userInputLowerCase);
                    userInputReversal = "";
                    
                    for i in reversed(range(z)):
                            userInputReversal += userInputLowerCase[i]

                    if userInputLowerCase == userInputReversal:
                        print(userInput + " is a palindrome")
                    else:
                        print(userInput + " is a not palindrome \nbecause it becomes " + userInputReversal + " when reversed")

                else:
                    print("The string you supplied contains not purely characters. Thanks.")
            else:
                print("The string you supplied contains only one(1) character. Thanks")
        else:
            print("The string you supplied contains not purely characters. Thanks.")
    else:
        print("The string you supplied contains not purely characters. Thanks.")
else:
    print("The string you supplied is empty. Thanks.")