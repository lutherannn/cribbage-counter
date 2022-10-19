import sys
import re

hand = []
numbers = []
suits = []
print("Format your hand with the card number and the suit with spaces between.")
print("For example: 2c 3d 4s 5h")
print(
    "Would be: The 2 of clubs, 3 of diamonds, 4 of spades, 5 of hearts."
)
handInput = input("Enter cards in hand: ")
cribCard = input("Enter the crib card in the same format as you entered your hand: ")

if len(handInput) != 11 and "10" not in handInput:
    print("Invalid cards in hand. Your hand should be 4 cards")
if "10" in handInput and len(handInput) != 12:
    print("Invalid cards in hand. Your hand should be 4 cards")

for x in handInput:
    if not x.isalpha() and not x.isdigit() and not x.isspace():
        print("Hand contains invalid characters.")
        sys.exit()
    if x.isdigit() or x == "j" or x == "q" or x == "k" or x == "a":
        if x.isalpha():
            numbers.append(x)
        else:
            numbers.append(int(x))
    if x.isalpha() and x != "j" and x != "q" and x != "k" and x != "a":
        suits.append(x)

for x in handInput.split():
    hand.append(x)

if len(cribCard) != 2:
    print("Invalid crib card, the crib card should only be one card.")

#Find pairs, each is worth 2 points
for x in numbers:
    if numbers.index(x) != 3:
        if x == numbers[numbers.index(x) + 1]:
            print("Pair found.")
            print(x, numbers[numbers.index(x) + 1])
print(hand, numbers, suits)
