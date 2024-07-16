s=''
for i in range(0,1000):
    s+='ciao a tutti ' + str(i)+'\n'

with open("lista.txt", "w") as file:
    file.write(s)