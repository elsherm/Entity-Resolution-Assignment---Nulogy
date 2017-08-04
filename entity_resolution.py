# -*- coding: cp1252 -*-
import csv
import re
import pandas as pd


#conversion = set('_"/.$-!``')
with open('C:\Users\mohamed\Downloads\Scholar.csv', 'rU') as Scholarcsvfile:
    Scholarreader = csv.reader(Scholarcsvfile, delimiter=',')
    Scholarwriter = csv.writer(open('Scholar_clean.csv', 'wb'), delimiter = ',')
    Scholarwriterlog = csv.writer(open('Scholar_missingdata.csv', 'wb'), delimiter = ',')

# removing Empty Scholar IDs and years
    for row in Scholarreader:
         if (len(row[0]) <=1):
             Scholarwriterlog.writerow(row)
         row[1]=re.sub(r'[-"/\.$?í€Œ¢í¢Œåí‰,ƒ\]\[ \t]', '', row[1])
         row[1] = str.upper(row[1])
         Scholarwriter.writerow(row)

Scholarcsvfile.close()

with open('C:\Users\mohamed\Downloads\DBLP1.csv', 'rU') as DBLPcsvfile:

     DBLPreader = csv.reader(DBLPcsvfile, delimiter=',')
     DBLPwriterlog = csv.writer(open('DBLP_duplicatedata.csv', 'wb'), delimiter = ',')
     DBLPwriter = csv.writer(open('DBLP_clean.csv', 'wb'), delimiter = ',')
# Removing Duplicates in DBLP1 based on title, author,and year
     entries=set()
     for row in DBLPreader:
        key = (row[1], row[2], row[4])
        if key in entries:
            DBLPwriterlog.writerow(row)

        row[1]=re.sub(r'[-"/\.$?í€Œ¢í¢Œåí‰,ƒ\]\[ \t]', '', row[1])
        row[1] = str.upper(row[1])
        entries.add(key)
        DBLPwriter.writerow(row)

DBLPcsvfile.close()

with open('DBLP_clean.csv', 'rb') as source:
    source_indices = dict((r[1],i) for i, r in enumerate(csv.reader(source)))
    
with open('DBLP_clean.csv', 'rb') as source:
    source_id = dict((i, r[0]) for i, r in enumerate(csv.reader(source)))
    #print source_id

with open('Scholar_clean.csv', 'rb') as scholar:
    with open('DBLP_Scholar_perfectMapping_Mohamed.csv', 'wb') as results:    
        reader = csv.reader(scholar)
        writer = csv.writer(results)

        writer.writerow(["idDBLP", "idScholar", "DBLP_Match","Scholar_Match","Match_ID"])
        next(reader)
        for row in reader:
            index = source_indices.get(row[1])

            if index is not None:
                writer.writerow([source_id.get(index),row[0],str(index),row[5],str(index)+"_"+str(row[5])])
results.close()

