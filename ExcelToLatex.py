excel = open('excel.txt','r')
data = excel.read()

def table(data):
    lines = data.split('\n')
    matrix = []
    for i in lines:
        line = i.split('\t')
        matrix.append(line)
    return matrix

table = table(data)

def latex(table):
    latex = ''
    for i in table:
        for n in range(len(i)):
            e = ""
            for let in i[n]:
                if let == ".":
                    e += ","
                else:
                    e += let
            i[n]=e
        line = ' $ & $ '.join(i)
        line = ' $ ' + line + ' $ \\\ ' + '\n'
        latex += line
    return latex

table = latex(table)
latex = open('latex.txt','w')
latex.write(table)

excel.close()
latex.close()
