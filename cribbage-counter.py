import sys
import re

hand = []

print("Format your hand with the card number and the suit with spaces between.")
print("For example: 2c 3d 4s 5h")
print(
    "Would be: The 2 of clubs, 3 of diamonds, 4 of spades, 5 of hearts, and the 6 of hearts"
)
handInput = input("Enter cards in hand: ")
cribCard = input("Enter the crib card in the same format as you entered your hand: ")

if len(handInput) != 11:
    print("Invalid cards in hand. Your hand should be 4 cards")

for x in handInput:
    if not x.isalpha() and not x.isdigit() and not x.isspace():
        print("Hand contains invalid characters.")
        sys.exit()
for x in handInput.split():
    hand.append(x)

if len(cribCard) != 2:
    print("Invalid crib card, the crib card should only be one card.")
