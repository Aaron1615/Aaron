'''

Excersize 1

Create a Program which takes the user's input of their name and age.
Then prints out both their name as well as the year they will turn 100.

Extra Credit:
1. Make all parts into their own functions, for added usability.

2. Require numbers for age and letter for names, stating when an input
is not in the proper format.

3. Ensures correct date by emphasizing specific age.

'''

from datetime import datetime


def main():
    name1 = name()
    age1 = age()
    now = datetime.now()  
    year = int(now.year)
    print ("Your name is {}".format(name1))
    if int(age1) > 100:
        print ("Wow, you were already 100 years old!")
    elif int(age1) == 100:
        print ("Wow, you are already 100 years old!")
    elif int(age1) < 100 and int(age1) > 0:
        year1 = (str(year - int(age1) + 100))
        print ("In the year {}".format(year1) + " you will be 100 years old.")
    else:
        print("You can't be negative years old!")



def name():
    while True:
        name = str(input("What is you're name? "))
        said = 0
        for x in name:  
            if not name.isalpha():
                if said <= 0:
                    print("That's not your name!")
                    said += 1
                    pass
            else:
                return (name)
                break
                

def age():
    while True:
        age = str(input("How old will you be turning this year? "))
        said = 0
        for x in age:
            if x.isalpha() and said <= 0:
                print("Numbers Please.")
                said += 1
                pass
            elif x.isalpha():
                pass           
        if said != 0:
            pass
        else:
            return age 
            break
    
                
main()