import os

def main(): 
    
    awp = findFolder('Chapters')
    relations = dict()  
    key = ''

    with open( awp + '\\buildChapters.tex', 'r') as f: 
        file = f.read().strip('\n').split("\n")

    for line in file: 

        if "\\import" in line: 
            line = line.replace('\\import','')
            line = line.replace('{','')
            line = line.replace('}','')
            relations = addentry(awp, line, relations)


    with open(os.path.join(os.getcwd(), "relations.txt"), 'w') as file: 

        for key in relations.keys():
            file.write(f'{key}:\n')
            for value in relations[key]:
                file.write(f"   {value[0]} by {value[1]}\n")
        
    

            
def addentry(awp, line, relations): 

    line.replace('.tex', '')
    line.replace('../Chapters/', '')
    line += '.tex'


    with open(awp + '\\' + line, 'r') as f: 
        file = f.read().strip('\n').split("\n")
        
        key = ''

    for row in file: 

        if '\\begin{define}' in row: 

            row == row.strip(" ")
            row = row.replace('\\begin{define}', '')
            row = row.replace('{','')
            row = row.replace('}','').strip(' ')
            relations[row] = relations.get(row,[])
            key = row

        while '\\rel' in row: 

            var1 = row[row.index('{') + 1 : row.index('}')].strip(' ')
            row = row[row.index('}') + 1: ]
            var2 =  row[row.index('{') + 1: row.index('}')].strip(' ')
            row = row[row.index('}') + 1: ].strip(" ")
            relation = (var1, var2)
            
            if relation not in relations.get(key, []):
                relations.get(key,[]).append(relation)

    return relations


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
    

if __name__ == "__main__": 
    main()