import string

symb = list(string.ascii_uppercase+'0123456789/)(-')

print(symb)

file = open("dataset2.txt", 'a')
""" 
for s in symb:
    for y in symb:
        for m in symb:
            for b in symb:
                file.write(s)
                file.write(y)
                file.write(m)
                file.write(b)
                file.write('\n') """


for s in symb:
    for y in symb:
        file.write(s)
        file.write(y)
        file.write('\n')
    