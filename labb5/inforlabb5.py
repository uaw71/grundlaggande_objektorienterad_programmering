#inför labb5
def main(): 
    glasslista = ['Nogger','Daimstrut']
    fortsatta = True
    while fortsatta:
        
        vald = getVal()
        print(vald)
        if vald == 1:
            addToGlassLista(glasslista)
        if vald == 2:
            print(glasslista)
        if vald == 3:
            uppdatLista = taBortElement(glasslista)
            print(uppdatLista)
        if vald == 0:
            print('Programmet är avslutat.')
            break
        
def getVal():
    val =int(input('Välj 1 för lägga till, 2 för att skriva ut,3 för att ta bort element i listan, 0 för att avsluta'))
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
    
def taBortElement(lista):
    i = int(input('Vilket element vill du ta bort?'))
    del lista[i]
    return lista

main()