# age=int(input("please enter your age"))
# if age > 18:
#     print("yes you can vote")
# else:
#     print("Please wait for next elections") 

# # Exercise: take a person's age, check if they are more than 16, if yes,
# # they can play in the basketball team 

# command=input("Enter 'exit' to end the program and 'continue' to keep the going")
# if command=="exit":
#     # write code that will take user out of cmd
#     print("existing cmd")
# elif command=="continue":
#     print("continue enjoying...")

# else:
#     print("wrong command")

# if - else- elseif chain
# print("_ " * 50)
# grade=float(input("What is your grade: "))
# if grade>80:
#     print("A grade👍")
# elif grade>70:
#     print("B👌")
# elif grade>60:
#     print("B+😊")
# elif grade>50:
#     print("c😉")
# elif grade>40:
#     print("sorry you cant do this")
# else:
#     print("Poooooooorr😪")

              
# a simple calculator
# taking inputs from the user........
# first_number=float(input("Enter first number: "))
# second_number=float(input("Enter second number: "))
# operator=input("Enter operator ")
# result=0

# if operator=="+":
#     result:first_number + second_number
#     print(f"Result is : {result}")
# elif operator=="-":
#     result:first_number - second_number
#     print(f"Result is : {result}")
# elif operator=="*":
#     result:first_number * second_number
#     print(f"Result is : {result}")
# elif operator=="/":
#     if second_number!= 0:
#        result=first_number/second_number
#        print(f"Result is : {result}")
#     else:
#         print ("division by 0 is not allowed") 


#     # handle it here, if second number is 0
# else:
#     print("Please check your operator sign again")

# Leap year exercise
year=int(input("Enter the year "))
if year%4==0 and year%100!=0 or year%400==0 :
    print("leap year")
else:
    print("Not a leap year")


year= int(input("Enter the year"))
if year %4==0:
    if year%100==0:
        if year %400!=0:
            print("leap year")
        else:
            print("leap year")
    else:
        print("leap year")
else:
    print("not a leap year")       


