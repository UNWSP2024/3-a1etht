#Programmer: Alethea Lo
#Date: 2/6/25

START

#//Define function to classify age

#This is the FUNCTION to run the classify_age(age):
if age >=0 and age <=12 then
return "Child"

else if age >=13 and <=19 then
return "Teenager"

else if age >=20 and <= 64 then
return "Adult"

else if age >=65 then
    return "Senior"

else
    return "Invalid age"//if age is negative or invalid

PRINT "Enter your age:"

#This is what the user will enter.

READ age//Take input from user

#This is the output:
result = classify_age(age) // Call the classify_age function

PRINT "You are classified as:", result//Output the result

END