import csv

# meta_file = "PanTHERIA_1-0_WR05_Aug2008.tsv"
meta_file = "../data/caviede_vidal_supp.csv"

# out_file = "./PanTHERIA_1-0_WR05_Aug2008.csv"
out_file = "../data/caviede_lower.csv"



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
with open(meta_file) as infile, open(out_file, 'w+') as outfile:
    reader = csv.reader(infile, delimiter=',')
    writer = csv.writer(outfile, delimiter=',')
    
    for row in reader:
        if count == 0:
            writer.writerow(row)
            count += 1
            continue
        row[1] = row[1].lower()
        writer.writerow(row)
            