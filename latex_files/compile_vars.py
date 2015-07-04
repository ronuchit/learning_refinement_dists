with open('variables.tex', 'r') as f:
    lines = f.readlines()

outlines = []
for l in lines:
    l = l.split('%%')
    comment = l[-1] if len(l) > 1 else ''
    l = l[0].split('%')
    command = l[-1] if len(l) > 1 else ''
    if comment:
        outlines.append('\\item[{}:] {}\n'.format(command, comment))

header = '\\section*{Notation}\n\\begin{itemize}\n'
footer = '\\end{itemize}'

with open('var_appendix.tex', 'w') as f:
    f.write(header)
    f.writelines(outlines)
    f.write(footer)

