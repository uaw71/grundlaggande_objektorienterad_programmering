#open file 
outfile = open('labb4test.txt', 'w')

#lägga till det som ska skrivas in i textfilen
for number in range(5):
    namn = input('Kompis du vill lägga till i kompislistan: ')
    
    print(namn + '\n')
    # lägga till i textfilen
    outfile.write(str(number+1) +' ' + namn + '\n')
    


#stäng textfilen
outfile.close()