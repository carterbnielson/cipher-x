# clearConsole function
def clearConsole():
    import os
    os.system("cls")
# end of clear console function

# display function
def display(originalText, encryptedText, plugs, horizontalRotation, verticalRotation):
    print(f"""Original Text: {originalText}
Encrypted Text: {encryptedText.upper()}

Current Plugs: {plugs}
Current Horizontal Rotation: {horizontalRotation}
Current Vertical Rotation: {verticalRotation}

Text Length: {len(encryptedText)}

Type "help" for commands
""")
# end of display function

# commands function
def commands():
    print("""\nCommands:

help: lists all commands
end: finalizes encryption and ends program
              
plug (pairs of letters): swaps two letters with each other
hrot (int): rotates characters around the list. positive for right, negative for left
vrot (int): rotates characters through the alphabet/integer series. positive for right, negative for left
""")
# end of commands functionyou