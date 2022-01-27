def main():
    glassLista = ['Nogger','Daimstrut']
    fortsatta = 0
    while(fortsatta == 0):
        vald = getVal()
        if vald == 1:
            addToGlassLista(glassLista)
        if vald == 2:
            print(glassLista)
        if vald == 3:
            removeFromLista(glassLista)
        if vald == 4:
            antal = len(glassLista)
            print(antal)

        fortsatta = int(input('För att fortsätta med listan välj 0'))


def getVal():
    val = int(input('Välj 1 för att lägga till, 2 skriva ut, 3 ta bort'))
    return val

def addToGlassLista(listan):
    valdGlass = input('Vilken glass vill du lägga till? ')
    listan.append(valdGlass)

def removeFromLista(listan):
    valdGlassRemove = input('Vilken glass vill du ta bort? ')
    listan.remove(valdGlassRemove)

main()