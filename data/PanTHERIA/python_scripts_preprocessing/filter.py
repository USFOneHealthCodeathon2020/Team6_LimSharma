'''
filtered out any items from Earth Microbiome data that was not:

+ kingdom: animalia
+ habitat: internal
'''
import csv

meta_file = "./13059_2019_1908_MOESM2_ESM.csv"

out_file = "./filtered.csv"



# p_class = 'mammalia'
# method = 'fecal'
p_kingdom = "animalia"
species = "homo"
habitat = 'internal'

### INDEXES
habitat_type = 24
method = 26
kingdom = 12
species = 11

count = 0
with open(meta_file) as infile, open(out_file, 'w') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        if count == 0:
            writer.writerow(row)
            count += 1
            continue
        if habitat in row[habitat_type] and p_kingdom in row[kingdom]:
            row[species] = row[species].lower()
            writer.writerow(row)
            