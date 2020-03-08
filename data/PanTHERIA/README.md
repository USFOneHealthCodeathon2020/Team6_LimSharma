# Dataset Information

## Panteria

There are two .csv's pulled directly from https://ecologicaldata.org/wiki/pantheria:

+ PanTHERIA_1-0_WR05_Aug2008
+ PanTHERIA_1-0_WR93_Aug2008

They were converted from tab-delimited to comma-delimited files. These were combined with the metadata from the Earth Microbiome Project using the python_scripts_preprocessing/combine.py script to generate panteria_microbe_combined.csv

## Body size allocation

bodyweight_microbe_meta.csv contains the content of panteria_microbe_combined.csv with the following additional processing:

+ Duplicates were removed (originally generated through the combine.py script - by accident)
+ All info from PanTHERIA was removed besides body mass
+ Body mass values were replaced with the allocations: big (> 58.7 kg), medium (>19.57 kg, <= 58.7 kg), and small(<= 19.57 kg). These were manually assigned to create approximately equal numbers of examples in each group.