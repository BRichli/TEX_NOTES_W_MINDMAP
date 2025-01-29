from sys import argv as args
import os

def main(): 

    contents = '\\begin{centering}\n{\\fontsize{30}{35}\\selectfont \\textbf{\\contentstitle}}\n\\vspace{30pt}\n'

    items = []
    awp = findFolder('Chapters')
    with open( awp + '\\buildChapters.tex', 'r') as f: 
        file = f.read().strip('\n').split("\n")

    for line in file: 
        if "\\import" in line: 
            line = line.replace('\\import','')
            line = line.replace('{','')
            line = line.replace('}','')
            items = addentry(awp, line, items)

    if items != []: 
        contents += '{\\fontsize{15}{16}\\selectfont\n\\begin{itemize}\n'
        for chaps in items: 
            contents += f'\\item {chaps[0]}' + '\n\\begin{itemize}\n'
            for defn in chaps[1]:
                contents += f'\\item {defn}\n'
            contents += '\\end{itemize}\n'
        contents += '\\end{itemize}}\n'
    contents += '\\end{centering}\n\\newpage'

    with open(awp + '\\contents.tex', 'w') as f: 
        f.write(contents)


def addentry(awp, line, items): 

    line = os.path.basename(line)
    if '.tex' not in line: 
        line += '.tex'

    with open(os.path.join(awp, line), 'r') as f: 
        file = f.read().strip('\n').split("\n")

    flag = True
    while(flag): 
        row = file.pop(0)
        if '\\chapter' in row: 
            row = row[row.index('{') + 1 : row.index('}')].strip(' ')
            chapname = "\\defchap{Chapter " + row + '}'
            flag = False

    temp = []
    for row in file:
        if '\\begin{define}' in row:
            row = row[row.index('}') + 1: ]
            thing = '\\deflink' + row[row.index('{') : row.index('}') + 1]
            temp.append(thing)
        
    items.append([chapname, temp])
    return items





def findFolder(name, depth = 2, retract = 2, limit = 5,  visited = [], awp = os.path.abspath(os.getcwd())): 

    if limit == 0: 
        return None
    visited.append(awp)
    dirs = os.listdir()
    if dirs == []:
        return None
    if name in dirs:
        return os.path.join(awp, name)
    if depth != 0:
        for dir in dirs:
            next = os.path.join(awp, dirs)
            if next in visited:
                continue
            maybe =  findFolder(name, depth - 1, retract + 1, limit -1, visited, next)
            limit -= 1
            if maybe is not None:
                return maybe
            
    if retract != 0:
        pardir = os.pardir(awp)
        return findFolder(name, depth + 1, retract - 1, limit -1, visited, pardir)



if __name__ == '__main__':

    main()