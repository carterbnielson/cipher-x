# plugboard function
def plugboard(originalText, plugLetters):
    # plugboard character list
    pl = []
    plugLetters = plugLetters.replace(", ", "")
    for i in range(len(plugLetters)):
        pl.append(plugLetters[i])
    # original text character list
    ot = []
    for i in range(len(originalText)):
        if originalText[i] == " ":
            ot.append("_")
        else:
            ot.append(originalText[i])
    
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