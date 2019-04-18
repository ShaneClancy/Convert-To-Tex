import csv
import sys
import os

def TableToTex(file_name, hline):
    #Check if input file from user exists
    if (not os.path.exists(file_name)):
        sys.stdout.write("Input file does not exist")
        return
    #open input and output files
    csvfile = open(file_name, 'r')
    csvfile = csv.reader(csvfile, delimiter=',')
    csvfile = list(csvfile)
    table = open('table.tex', 'w')
    sys.stdout = table

    #write table baginning
    sys.stdout.write('\\begin{tabular}{')
    #calculate and write column syntax
    rowSize = (len(csvfile[0]))
    for i in range(rowSize):
        sys.stdout.write('|c')
    #end table beginning
    sys.stdout.write('|}\n')

    for i in csvfile:
        #print out horizontal line if user specifies
        if (hline == 1):
            sys.stdout.write('\t\\hline\n\t')
        else:
            sys.stdout.write('\t')
        
        for j in (range(rowSize - 1)):
            sys.stdout.write(str(i[j]) + ' ' + '& ')
        sys.stdout.write(str(i[rowSize - 1]) + ' \\\\\n')
    
    sys.stdout.write('\\end{tabular}\n')
    return
