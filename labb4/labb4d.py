#läsa från labb4.txt
infile = open('labb4.txt', 'r')
counter = 0
#contentTxtFile = ''

for line in infile:
    print(line, end = '')
    #contentTxtFile = contentTxtFile + ' ' + line.rstrip("\n")
    counter +=1

infile.close()
print(f'totalt antal kompisar i textfilen: {counter}')
#print(contentTxtFile)