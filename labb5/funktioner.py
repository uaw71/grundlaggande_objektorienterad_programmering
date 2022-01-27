#funktioner
#skapa en enkel funktion och anropa den
#def följt av funktionsnamnet. Inom funktionens parentes anger man om det finns några inparametrar,
#om något behövs för att funktionen ska kunna utföra det som den ska göra
#efter definitionen följer funktionsdokumentation som förklarar vad funktionen gör.
#Därefter följer kodsatser (indenterade) med det som funktionen ska utföra när den anropas.
#Om funktionen ska returnera något så avslutar man med att skriva return och vad den ska returnera (leverera).
def getInput():
    "Funktion som hämtar input från användaren och returnerar en int"
    inputVariabel = int(input('Välj ett tal?'))
    return inputVariabel

print(getInput())

#för att hämta funktionsdokumentationen skriv help(funktionsnamnet):
help(getInput)
