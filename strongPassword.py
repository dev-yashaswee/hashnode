def isStrong(password):
    if(len(password)<8):
        return False
    symbols     = "@%^"
    hasCapAlpha = False
    hasDigit    = False
    hasSymbol   = False
    for char in password:
        if(char in symbols):
            hasSymbol = True
        elif(char.isupper()):
            hasCapAlpha = True
        elif(char.isdigit()):
            hasDigit = True
        else:
            if(not char.isalpha()):
                return False
    return hasCapAlpha and hasDigit and hasSymbol
def display(isStrong):
    return "Valid" if isStrong else "Invalid"

password = input()
print(display(isStrong(password)))
