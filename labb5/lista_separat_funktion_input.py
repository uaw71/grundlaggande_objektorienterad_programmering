#lista_separat_funktion_input
def main():
    calcMedel(addToList())

def addToList():
    fortsatta = 0
    resLista = []
    while fortsatta == 0:
        resultat = int(input('Mata in resultat: '))
        resLista.append(resultat)
        fortsatta = int(input('För fortsatta skriv 0, annars 1: '))
    print(f'De inmatade resultaten är: {resLista}')
    print()
    return resLista

def calcMedel(lista):
    total = 0
    for res in lista:
        total += res
    medel = total /len(lista)
    print(f'Medelvärdet av resultaten är: {medel}\n')

main()