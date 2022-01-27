namnen = ''
for num in range(5):
    namn = input('lägg till ett namn: ')
    print(f'nr. {num+1} namn: {namn}')
    namnen = namnen + ' ' + namn
print(namnen)