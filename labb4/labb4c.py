another ='y'
nr = 0

#open file 
outfile = open('labb4.txt', 'w')

while another == 'y' or another == 'Y':
    namn = input('Kompis du vill lägga till i kompislistan: ')
    nr+=1
    print(namn + '\n')
    # lägga till i textfilen
    outfile.write(str(nr) +' ' + namn + '\n')
    another = input('Skriv y för att lägga till en till kompis ')
    

#stäng textfilen
outfile.close()

#läsa från labb4.txt
infile = open('labb4.txt', 'r')
counter = 1
#contentTxtFile = ''

for line in infile:
    print(line, end ='')
    #contentTxtFile = contentTxtFile + ' ' + line.rstrip("\n")
    counter +=1

infile.close()
print(f'totalt antal kompisar i textfilen: {counter-1}')
#print(contentTxtFile)