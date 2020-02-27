import csv
import pandas as pd

pantheria_1 = "pantheria_combined.csv"
# pantheria_2 = "PanTHERIA_1-0_WR93_Aug2008.csv"
micro_file = "filtered_internal_animalia.csv"

outfile = "test.csv"

df_1 = pd.read_csv(pantheria_1)
# df_2 = pd.read_csv(pantheria_2)
df_3 = pd.read_csv(micro_file)

# df_merged = df_3.merge(df_1, left_on="host_scientific_name", right_on=df_2.columns[4], how="outer")
# df_merged = df_3.merge(df_2, left_on="host_scientific_name", right_on=df_2.columns[4], how="outer")

df_merged = pd.merge(df_3, df_1, left_on="host_scientific_name", right_on=df_1.columns[4], how="left")
# df_merged = pd.merge(df_merged, df_2, left_on="host_scientific_name", right_on=df_2.columns[4], how="left")

df_merged.to_csv(outfile, index=False)

# with open(pantheria_1, 'r') as animal_1, open(panteria_2, 'r') as animal_2, open(micro_file, 'r') as microb, open(outfile, 'w') as final_f:
#     animalR1 = csv.reader(animal_1, delimiter=',')
#     animalR2 = csv.reader(animal_2, delimiter=',')
#     microR = csv.reader(microb, delimiter=',')

#     final = csv.writer(final_f, delimiter=',')



#     print(microR.rows[0])