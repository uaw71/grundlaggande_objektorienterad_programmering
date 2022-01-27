#lista_funtion

def main():
    resLista = [30,45,23,56,67]
    total = 0
    for res in resLista:
        total += res
    medel = total /len(resLista)
    print(f'Medelvärdet av resultaten är: {medel}')

main()