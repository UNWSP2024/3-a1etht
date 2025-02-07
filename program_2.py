#Programmer: Alethea Lo
#Date: 2/6/25

#Asking the user to input an age
age=int(input("Please enter the person's age:"))

#Apply the age range that displays the corresponding message
if age <=1:
    print("The person is an infant.")
elif 1<age<13:
    print("The person is a child.")
elif 13<=age<20:
    print("The person is a teenager.")
else:
    print("The person is an adult.")