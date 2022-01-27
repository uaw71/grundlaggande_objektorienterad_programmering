#add to list
#fleraTal = input('skriv flera tal: ')
#ls = fleraTal.split()
#for e in ls:
#    print(e)

#print(ls)

#ls.remove('jag')
#print(ls)

talLista = []
fortsatta = 0
i = 0
while fortsatta == 0:
    inmatatTal = int(input('lägg till ett tal'))
    talLista.insert(i, inmatatTal)
    i+=1
    fortsatta = int(input('fortsatta =0'))

print(talLista)