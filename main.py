# imports
from encrypt import *
from functions import *

# startup and input
clearConsole()
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
clearConsole()

# variable init
encryptedText = text
plugs = "none"
horizontalRotation = "none"
verticalRotation = "none"
encrypting = True
key = ""

# input loop
while encrypting:
    display(originalText, encryptedText, plugs, horizontalRotation, verticalRotation)
    userInput = input("> ").lower()

    # input logic
    # detect help command
    if userInput == "help":
        commands()
    # detect end command
    elif userInput == "end":
        clearConsole()
        print(f"Original Text: {originalText}\nEncrypted Text: {encryptedText.upper()}\nKey: {key.upper()}")
        encrypting = False
    # detect plug command
    elif "plug" in userInput:
        userInput = userInput.replace("plug ", "")
        if "_" in userInput:
            clearConsole()
            print("Can't replace that character, try again\n")
            pass
        else:
            encryptedText = plugboard(encryptedText, userInput)
            key += "#" + userInput.replace(" ", "")
            clearConsole()
        continue
    # detect hrot command
    elif "hrot" in userInput:
        userInput = userInput.replace("hrot ", "")
        if int(userInput) > len(encryptedText) - 1:
            clearConsole()
            print("Redundant input, try again\n")
            pass
        elif int(userInput) < -len(encryptedText) + 1:
            clearConsole()
            print("Redundant input, try again\n")
            pass
        else:
            encryptedText = horizontalRotor(encryptedText, userInput)
            key += "$" + userInput
            clearConsole()
        continue
    # detect vrot command
    elif "vrot" in userInput:
        userInput = userInput.replace("vrot ", "")
        if int(userInput) > 25:
            clearConsole()
            print("Bad input, try again\n")
            pass
        elif int(userInput) < -25:
            clearConsole()
            print("Bad input, try again\n")
            pass
        else:
            encryptedText = verticalRotor(encryptedText, userInput)
            key += "%" + userInput
            clearConsole()
        continue
    else:
        print("Command not recognized")