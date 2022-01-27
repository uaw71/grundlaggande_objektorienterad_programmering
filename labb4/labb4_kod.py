# labb4
import random
summa = 0
mvg = 0
vg = 0
g = 0
u = 0

outfile = open('resultat.txt', 'w')
for nr in range(145):
    slumpatResultat = random.randint(45,100)
    #print(slumpatResultat)
    outfile.write(str(slumpatResultat) + '\n')

outfile.close()

infile = open('resultat.txt', 'r')

for line in infile:
    intLine = int(line)
    summa  += intLine
    if intLine >=90:
        mvg += 1
    elif intLine >= 76:
        vg += 1
    elif intLine >= 60:
        g += 1
    else:
        u += 1

infile.close()

print(f'Summan är: {summa}')
print(f'Antal resultat med MVG: {mvg}')
print(f'Antal resultat med VG: {vg}')
print(f'Antal resultat med G: {g}')
print(f'Antal resultat med U: {u}')
godkantres = mvg + vg + g
print(f'Antal resultat som inte är underkänt g-mvg: {godkantres}')
procentGodkandaRes = godkantres/145
procentGodkandaRes *= 100
print(f'Procent godkända resultat: {procentGodkandaRes :.1f} %')
medel = summa/145
print(f'Medelvärdet av resultatet är: {medel :.1f}')

