#labb5
#program som visar meny och alternativ för att lägga till, ta bort, söka, ändra, skriva ut

def valMeny():
    val = int(input('Meny att välja från: \nLägga till välj 1 \nTa bort = 2 \nSöka = 3 \nÄndra = 4 \nSkriva ut = 5\n'))
    
    return val

print(valMeny())
