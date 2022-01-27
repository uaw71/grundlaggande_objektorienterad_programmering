#listor
glasslista = ['nogger','daimstrut','cornetto','magnum']
print(glasslista)
print(glasslista[2])

indexforValdGlass = glasslista.index('magnum')
print(indexforValdGlass)

glasslista.append('cola')
print(glasslista)

glasslista.insert(3,'piggelin')
print(glasslista)

print(len(glasslista))

glasslista.sort()
print(glasslista)

glasslista.remove('cornetto')
print(glasslista)

del glasslista[1:3]
print(glasslista)

glasslista.clear()
print(glasslista)

glassTuple = ('nogger','daimstrut')
print(glassTuple)
print(len(glassTuple))
