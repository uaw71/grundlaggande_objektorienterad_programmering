#funktioner2
def getInput():
    "Funktion som hämtar input från användaren och returnerar en int"
    inputVariabel = int(input('Välj ett tal?'))
    return inputVariabel

sum = 0
#en for loop som hämtar input från användare med hjälp av getInput() funktionen
#och summerar ihop talen som användaren matat in.
for x in range(3):
    tal = getInput()
    print(tal)
    sum += tal
print(f'Summan av talen är: {sum}') 
