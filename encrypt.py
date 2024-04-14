# plugboard function
def plugboard(originalText, plugLetters):
    # plugboard character list
    pl = []
    plugLetters = plugLetters.replace(" ", "")
    for i in range(len(plugLetters)):
        pl.append(plugLetters[i])
    # original text character list
    ot = []
    for i in range(len(originalText)):
        if originalText[i] == " ":
            ot.append("_")
        else:
            ot.append(originalText[i].lower())
    # perform plugboard encryption
    for i in range(len(ot)):
        for j in range(len(pl)):
            if j % 2 == 0:
                if ot[i] == pl[j]:
                    ot[i] = pl[j + 1]
                else:
                    pass
            else:
                pass
    # output encrypted text
    return "".join(ot)
# end of plugboard function

# horizontalRotor function
def horizontalRotor(originalText, rotorNumb):
    # original character text list
    ot = []
    for i in range(len(originalText)):
        if originalText[i] == " ":
            ot.append("_")
        else:
            ot.append(originalText[i].lower())
    # rotor number init
    rn = -int(rotorNumb)
    # rotate list
    ot = ot[rn:] + ot[:rn]
    # output rotated list
    return "".join(ot)
# end of horizontalRotor function

# verticalRotor function
def verticalRotor(originalText, rotorNumb):
    # lower case values
    lowerCaseVals = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
    integerVals = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
    # original character text list
    ot = []
    for i in range(len(originalText)):
        if originalText[i] == " ":
            ot.append("_")
        else:
            ot.append(originalText[i].lower())
    # rotor number init
    rn = int(rotorNumb)
    # rotate list
    for i in range(len(ot)):
        ot[i] = ord(ot[i])
        if ot[i] in lowerCaseVals:
            ot[i] = ot[i] + rn
            if ot[i] > 122:
                difference = ot[i] - 122
                ot[i] = 96 + difference
            elif ot[i] < 97:
                difference = 97 - ot[i]
                ot[i] = 123 - difference
            else:
                pass
        elif ot[i] in integerVals:
            ot[i] = ot[i] + rn
            if ot[i] > 57:
                difference = ot[i] - 57
                ot[i] = 47 + difference
            elif ot[i] < 48:
                difference = 48 - ot[i]
                ot[i] = 58 - difference
            else:
                pass
        elif ot[i] == 95:
            pass
    # convert back to character
    for i in range(len(ot)):
        ot[i] = chr(ot[i])
    # output rotated list
    return "".join(ot)
# end of verticalRotor function