def getInput():
    "Funktion som hamtar input fran anvandare och returnerar en int"
    inputVariabel = int(input('Välj ett tal '))
    return inputVariabel

"""sum = 0
for x in range(3):
    tal = getInput()
    print(tal)
    sum  += tal
print(f'Summan av talen är: {sum}')"""

def calcKub(x):
    kubVol = x*x*x
    return kubVol

print(calcKub(4))
