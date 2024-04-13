# get input
# turn input all lower case
# encrypt
# print encrypted message and key

# imports
from encrypt import *

# input
print("Please enter a string of text to start (Letters, integers, and spaces only)")
originalText = input("> ")

# convert input to list
text = []
for i in range(len(originalText)):
    text.append(originalText[i])

# format input
for i in range(len(text)):
    if text[i] == " ":
        text[i] = "_"
    else:
        text[i] = text[i].lower()
text = "".join(text)

# test output
print(text)

"""
Original Text: {Original Text}
Encrypted Text: {Encrypted Text}

Current Plugs: {Plugs}
Current Horizontal Rotation: {Horizontal Rotation}
Current Vertical Rotation: {Vertical Rotation}

Type "help" for commands

>
"""