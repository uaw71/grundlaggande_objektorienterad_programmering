#lista
glasslista = ['nogger', 'daimstrut', 'cornetto','magnum']
print(glasslista)
#skriva ut på enskilt index
print(glasslista[2])

#för att få fram index för visst element
indexGlasslista = glasslista.index('daimstrut') 
print('Index för daimstrut är: ', indexGlasslista)

#lägga till element sist i listan
glasslista.append('88:an')
print(glasslista)

#lägger till element på specifik position i listan, index 3
glasslista.insert(3, 'piggelin')
print(glasslista)

#sortera listan i bokstavsordning
glasslista.sort()
print(glasslista)

#ta bort element från listan
glasslista.remove('88:an')
print(glasslista)
#ta bort enstaka element eller skivor (slices) härnedan element 1 och 2
del glasslista[1:3]
print(glasslista)
#tömma listan
glasslista.clear()
print(glasslista)
