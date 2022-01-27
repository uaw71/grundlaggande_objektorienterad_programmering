#lista_funktion_input
def main():
    fortsatta = 0
    resLista = []
    while fortsatta == 0:
        resultat = int(input('Mata in resultat: '))
        resLista.append(resultat)
        fortsatta = int(input('För fortsatta skriv 0, annars 1: '))
    print(f'De inmatade resultaten är: {resLista}')
    print()
    total = 0
    for res in resLista:
        total += res
    medel = total /len(resLista)
    print(f'Medelvärdet av resultaten är: {medel}\n')

main()