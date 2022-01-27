outfile = open('textF.txt', 'w')

outfile.write('kalle' + '\n')
outfile.write('janne' + '\n')
outfile.write('majsan'+'\n')

outfile.close()
#read from textfile and save in a list
f = open('textF.txt', 'r')
lista = f.read().splitlines()
print(lista)
f.close()

