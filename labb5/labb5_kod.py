#inför labb5
def main(): 
    glasslista = ['Nogger','Daimstrut', 'Magnum', 'Piggelin','Cornetto']
    fortsatta = True
    while fortsatta:
        
        vald = getVal()
        print(vald)
        if vald == 1:
            addToGlassLista(glasslista)
        if vald == 2:
            addToSpecificIndex(glasslista)
            print(f'Uppdaterad {glasslista}')
        
        if vald == 3:
            uppdatLista = taBortIndexpos(glasslista)
            print(uppdatLista)
        if vald == 4:
            uppdatLista = taBortElement(glasslista)
            print(uppdatLista)
        if vald == 5:
            emptyList(glasslista)
        if vald == 6:
            print(listLen(glasslista))
        if vald == 7:
            print(glasslista)
        if vald == 8:
            print(printVaraSpecifiktIndex(glasslista))
        if vald == 9:
            sorteraListan(glasslista)
        if vald == 0:
            print('Programmet är avslutat.')
            break
        
def getVal():
    val =int(input('Välj 1 för lägga till\
         \n2 lägga till på specifikt index\
          \n3 ta bort vara position, 4 ta bort vara namn, 5 tömma hela shopping listan, 7 för att skriva ut, 8 skriv ut vara specifikt index, 9 sortera listan, 0 för att avsluta '))
    return val
   
def addToGlassLista(addlista):
    fortsatta = 0
    while fortsatta == 0:
        glass = input('Lägg till glass: ')
        addlista.append(glass)
        fortsatta = int(input('fortsatta = 0'))
        print()#tom rad
    print(addlista)
    return addlista

def addToSpecificIndex(insertLista):
    plats = int(input('På vilken plats ska ny glass läggas till?'))
    glassNamn = input('Glassnamn?')
    insertLista.insert(plats, glassNamn)
    return insertLista
    
def taBortIndexpos(lista):
    i = int(input('Vilket index vill du ta bort?'))
    del lista[i]
    return lista

def taBortElement(lista):
    taBortGlass = input('Vilken glass vill du ta bort? ')
    for item in lista:
        if item == taBortGlass: 
            lista.remove(taBortGlass)
            break
    else:
        print('Glassen finns inte i listan.')
    return lista

def emptyList(lista):
    lista.clear()
    print(lista)
    return lista

def listLen(lista):
    antalElementILista = len(lista)
    #print(antalElementILista)
    return antalElementILista

def printVaraSpecifiktIndex(lista):
    valtIndex = int(input('Vilket index vill skriva ut innehållet för? '))
    if valtIndex <= listLen(lista)-1:
        valueAtIndex = lista[valtIndex]
    else:
        print(f'Valt index finns inte. Välj mellan 0 - {listLen(lista)-1}')
        valtIndex = int(input('Vilket index vill skriva ut innehållet för? '))
        valueAtIndex = lista[valtIndex]
    return valueAtIndex

def sorteraListan(lista):
    lista.sort()
    print(lista)
    return lista

main()