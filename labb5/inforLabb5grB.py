def main():
    glasslista = ['nogger', 'daimstrut']
    fortsatta = True
    while fortsatta:
        val = int(input('Välj 1 för att lägga till \nvälj 2 för att skriva ut \nvälj 3 för att ta bort\nvälj 0 för att avsluta'))
        print(val)
        if val == 1:
            addToGlassLista(glasslista)
        
        if val == 2:
            print(glasslista)
        if val == 3:
            #uppdatLista = taBortElement(glasslista)
            print(taBortElement(glasslista))

        if val == 0:
            print('Programmet är avslutat')
            break

def addToGlassLista(addLista):
    fortsatta = 0
    while fortsatta == 0:
        glass = input('Lägg till namn på glass: ')
        addLista.append(glass)
        fortsatta = int(input('För att lägga till en glass till tryck 0, annars 1'))
        print()
    print(addLista)
    return addLista

def taBortElement(lista):
    i = int(input('Vilken indexposition vill du ta bort? '))
    del lista[i]
    return lista

main()