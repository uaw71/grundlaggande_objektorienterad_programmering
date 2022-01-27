#lägga till det som ska skrivas in i textfilen
namn1 = input('Kompis du vill lägga till i kompislistan: ')
namn2 = input('Kompis du vill lägga till i kompislistan: ')
namn3 = input('Kompis du vill lägga till i kompislistan: ')

#open file 
outfile = open('labb4.txt', 'w')

outfile.write(namn1 + '\n')
outfile.write(namn2 + '\n')
outfile.write(namn3 + '\n')

#stäng textfilen
outfile.close()