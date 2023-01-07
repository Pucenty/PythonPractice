#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

concat = ""

for i in range(nr_letters):
    print(f"letters i={i}")
    concat += random.choice(letters)
for i in range(nr_numbers):
    print(f"numbers i={i}")
    concat += random.choice(numbers)
for i in range(nr_symbols):
    print(f"symbols i={i}")
    concat += random.choice(symbols)

print(f"concat = {concat}")

# concat_as_list = list(concat)
# print(concat_as_list)
# random.shuffle(concat_as_list)
# print(concat_as_list)
#
# print(''.join(concat_as_list))

random_pass = ""
concat_as_list = list(concat)
print(f"concat_as_list {concat_as_list}, concat_as_list length = {len(concat_as_list)}")

i = 1
for j in concat:
    print(f"Looping for {i} time")
    choice = random.choice(concat_as_list)
    print(f"Random choice is {choice}")
    random_pass += choice
    print(f'Current random_pass = {random_pass}')
    concat_as_list.remove(choice)
    print(f'Current concat_as_list content:{concat_as_list}')
    i += 1

print(f"Final random pass is: {random_pass}")



