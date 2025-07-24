# # for loop
# # 1. starting point
# # 2. Condition
# # 3. Increment or Decrement
# # Database of people
# names=["Will","Leo","Kate","Kay","Afumbom","Atimbom","beribom"]
# print(names[0])
# print(names[1])
# print(names[2])

# count=1
# for name in names:
#     print(name)
#     print(f"{count}.{name}")
#     if name.endswith("bom"):
#         print(f"We dan catch you: {name}")
#     else:
#         print(f"Welcome to the party: {name}")

# my_name="beribom"
# for letter in my_name:
#     print(f"letter: {letter}")

# range    
# for i in range(5):
#     print(i)


# for i in range(0, 10, 2,):
#     print(i)


# for i in range(2,7):
#     print(1)

# for i in range(10, 0, -2):
#     print(f"countdown: {i}")
# print("blast off! 🚀")

# Basic while loop
# count = 1
# while count <=5:
#     print(f"count is: {count}")
#     count += 1 

# print("Finding the first even number:")
# for number in range(1, 10):
#     if number % 2 == 0:
#         print(f"Found even number: {number}")
#         break
#     print(f"{number} is odd")


# user_input = ""
# while user_input != "quit":
#     user_input = input("Enter 'quit' to exit: ")
#     if user_input != "quit":
#         print(f"you entered: {user_input}")
# print("Goodbye!")


# Nested loop

# Multiplication table
# print("Multiplication Table:")
# for i in range(1, 4):
#     for j in range(1, 4):
#         result = i * j
#         print(f"{i} * {j} = {result}")
#     print()


print("Multiplication table:")
for i in range(1, 20):
    for j in range(1, 20):
        result = i * j
        print(f"{i} * {j} = {result}")
    print()
    
       

