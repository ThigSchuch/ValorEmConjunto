import time

files = ["dataset-1-a.csv","dataset-1-b.csv","dataset-1-c.csv"]
saida = ["resposta-dataset-1-a.txt","resposta-dataset-1-b.txt","resposta-dataset-1-c.txt"]

def openFile(file):
    arq = open(file,"r")
    lines = arq.read().split("\n")
    arq.close()
    return lines

def appendFile(file, text):
    arq = open(file,"a")
    arq.write(text)
    arq.close()

def checkInside(number, lines):
    for i in range(2,len(lines),1):
        if lines[i] == number:
            return i
    return -1

for i in range(3):
    start_time = time.time()
    lines = openFile(files[i])
    first = lines[0]
    position = checkInside(first, lines)
    
    if position == -1:
        appendFile(saida[i], "False\n")
    else:
        appendFile(saida[i], "True\n")

    appendFile(saida[i], str(position)+"\n")
    appendFile(saida[i], str(time.time() - start_time))