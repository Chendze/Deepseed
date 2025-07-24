# Password = input("Enter your password:")
# Lower_case = Password.islower()
# Upper_case = Password.isupper()
# Numeric = Password.isdigit()

# if Lower_case and Upper_case and Numeric:
#     print("This a strong password")
# else:
#     print("Please do it again")

password = input("Enter your password:")
Lower_case = password.islower()
Upper_case = password.isupper()
Numeric = password.isdigit()

if Lower_case and Upper_case and Numeric:
    print("This a strong password")
else:
    print("Please do it again")
    
    
l = False
u = False
d = False

password = input("Enter your password:")

for letter in password:
    if letter.islower():
        l = True
    elif letter.isupper():
        u = True
    elif letter.digit():
        d = True

if l and u and d:
    print("Strong password")
else:
    print("Weak password")                    

