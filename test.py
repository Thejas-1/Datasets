import os
import csv
from collections import defaultdict
import math

directory1 = 'Astronomy'
directory2 = 'Astrophysics'
directory3 = 'Machine_Learning'

number_of_files = len([item for item in os.listdir(directory1) if os.path.isfile(os.path.join(directory1, item))])

a = number_of_files
b = os.listdir(directory1)

print a,b

listofd1 = []
listofd2 = []
listofd3 = []

columns = defaultdict(list) # each value in each column is appended to a list
#listofd = []


for h in b:
    i1 = directory1 + '/' + h 
    with open(i1) as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value 
                columns[k].append(v)
        listofd1.append(row)

b = os.listdir(directory2)
for h in b:
    i1 = directory2 + '/' + h 
    with open(i1) as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value 
                columns[k].append(v)
        listofd2.append(row)

b = os.listdir(directory3)
for h in b:
    i1 = directory3 + '/' + h 
    with open(i1) as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value 
                columns[k].append(v)
        listofd3.append(row)
inf = []
nlist = []
s=0
val=0
temp = []
#print listofd3

print '\n',"Astronomy"
for columns in listofd1:
    for key, value in columns.iteritems():
        inf.append((50/3.14)*math.exp((3.14**(2))*100/(50**(2)))*math.sin(3.14*int(value[0])/50));
        #print inf
    j = inf[0]
    s = 0
    val = 0
    for a in inf:
        s = s+1
	if a>j:
            j = a
	    val = s
    for key, value in columns.iteritems():
        akey = key
        temp.append(akey)

    print temp[val]  
    del temp[:]
    del inf[:]

print '\n',"Astrophyics"
for columns in listofd2:
    for key, value in columns.iteritems():
        inf.append((50/3.14)*math.exp((3.14**(2))*100/(50**(2)))*math.sin(3.14*int(value[0])/50)+40);
        #print inf
    j = inf[0]
    s = 0
    val = 0
    for a in inf:
        s = s+1
	if a>j:
            j = a
	    val = s
    for key, value in columns.iteritems():
        akey = key
        temp.append(akey)

    print temp[val]  
    del temp[:]
    del inf[:]
#print nlist

print '\n',"Machine Learning"
for columns in listofd3:
    for key, value in columns.iteritems():
        inf.append((50/3.14)*math.exp((3.14**(2))*100*5/(50**(2)))*math.sin(3.14*int(value[0])/50)+40);
        #print inf
    j = inf[0]
    s = 0
    val = 0
    for a in inf:
        s = s+1
	if a>j:
            j = a
	    val = s
    for key, value in columns.iteritems():
        akey = key
        temp.append(akey)

    print temp[val]  
    del temp[:]
    del inf[:]

"""for h in nlist:
    print h
    j = h[0]
    for a in h:
        s = s+1
        if a>j:
	    j = a
	    val = s

print s,j
#print columns[s]

print f
"""

	
#for key, value in row.iteritems():
#    print key
