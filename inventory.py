# ECE 2524 Homework 5 Problem 1 Randall Ferrance

import sys
import fileinput
import argparse
import ast
import operator

parser = argparse.ArgumentParser(description='Positional arguements.')
parser.add_argument('-f', '--data-file', type=str, help='path to the data file to read at startup')
args = parser.parse_args()

items = []
listOf = []


def makeList():
    for line in fileinput.input(args.data_file):
        newline = ' '.join(line.split())
        try:
            dict1 = {'PartID':newline.split(' ')[0],'Description':newline.split(' ')[1],'Footprint':newline.split(' ')[2],'Quantity':newline.split(' ')[3]}
            items.append(dict1)
        except IndexError as e:
            sys.stderr.write('Invalid input file, please check readme for help')
        
            
def addItem(newItem):
    items.append(ast.literal_eval(newItem))
    print 'Done\n'
    return items
    
def listItems(value):
    if (value=='all'):
        print 'DATA'
        for x in items:
            print '%10s %30s %10s %10s' %(x['PartID'], x['Description'], x['Footprint'], x['Quantity'])
    else:
        try:
            row=value.split('=')[0]
            number=value.split('=')[1]
            print 'DATA'
            for x in items:
                if(x[row]==number or x[row]==row):
                    print '%10s %30s %10s %10s' %(x['PartID'], x['Description'], x['Footprint'], x['Quantity'])
        except IndexError as e:
            sys.stderr.write('Invalid input, please check readme for help')
    print '%%\n'
    return items
                
def removeItem(value):
    try:
        row = value.split('=')[0]
        number = value.split('=')[1]
        for x in items:
            if(x[row]==number):
                items.remove(x)
        print 'Done\n'
        return items
    except IndexError as e:
        sys.stderr.write('Invalid input, please check readme for help')
    
def setItem(value):
    try:
        new = value.split(':')[0]
        old = value.split(':')[1]
        newarg = new.split('=')[0]
        newval = new.split('=')[1]
        oldarg = old.split('=')[0]
        oldval = old.split('=')[1]
        for x in items:
            if(x[oldarg]==oldval):
                x[newarg]=newval
        print 'Done\n'
        return items
    except IndexError as e:
        sys.stderr.write('Invalid input, please check readme for help')
    
def sortItems(value):
    dict1 = items.pop(0)
    if(value=='Quantity'):
        items.sort(key=lambda x: float(x['Quantity']))
    else:
        items.sort(key=operator.itemgetter(value))
    items.insert(0,dict1)
    print 'Done\n'
    return items
    
functions = {'add':addItem,'list':listItems,'remove':removeItem,'set':setItem, 'sort':sortItems}
makeList()

listItems('all')
            
for line in iter(sys.stdin.readline,""):
    listOf.append(line)
        
for line in listOf:  
    try:      
        action = line.split(' ')[0]
        value = line.split(' ')[1]
        value = value.strip()
        

        items = functions[action](value)
    except KeyError as e:
        sys.stderr.write('Invalid input.\n')
    except IndexError as e:
        sys.stderr.write('Please use two arguements, see readme for help.\n')
        

fout = open(args.data_file, 'w')
for x in items: 
    fout.write(x['PartID']+'\t'+ x['Description']+ '\t'+ x['Footprint']+'\t'+ x['Quantity']+'\n')


