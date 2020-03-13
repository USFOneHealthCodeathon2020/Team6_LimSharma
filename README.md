# Team Animal
<b>Team leads</b> (in alphabetical order): Jean Lim and Ravi Sharma <br>
<b>Team members</b> (in alphabetical order): Maddie Barrow, Khandaker Tasnim Huq, Youngchul Kim, Ojas Natarajan, Matt Sumpter <br>
<b>Faculty advisor</b>: Lynn Martin

## :: About our Project::

### Introduction
We applied unsupervised learning to animal microbiome data from the Earth Microbiome Project (http://www.earthmicrobiome.org and https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6996194/) to determine how microbial communities cluster among host species.  We then used other databases to find correlations with various host traits to start to explain the existence of these patterns.​

### What is the problem you want to solve?​
Are there generalities about microbial communities across multicellular forms of life? Do particular host traits (e.g., size, diet, and phylogeny) drive them?​

### Why does it matter?​
The scale and dynamic nature of microbial diversity is staggering. Our hope is to reveal general patterns of microbial community organization to serve as a baseline for deeper investigation.​  Our work could also implicate host species where microbial diversity should be exceptionally high, which could provide a source of microbes with novel metabolic effects.

### Why is it challenging?​
The field is fairly new, so sampling of host microbiota diversity is at present fairly sparse. It is currently known that diet, host phylogeny, and few other environmental factors shape host-microbiome assemblies. However, other potential effects on host-associated microbiomes across species, including size and host life history, have been understudied. A comprehensive analysis on drivers of animal microbiomes is challenging but can yield new insights on host-microbiome associations.​

### Why are you excited about it?​
A broader perspective such as this one can serve as a solid foundation from which more targeted studies can start.  The opportunity to gain insight into host-microbe associations across the scope of animal life is also compelling.​

### What do you need to make it happen?​
Appropriate data and expertise in microbiomes, evolutionary biology, machine learning, statistical analysis and computer programming…and luck and $$ wouldn’t hurt.

## :: Workflow ::

### Data collection
Rarefied OTU table (1000 reads per sample) and metadata of internal animal microbiomes from the Earth Microbiome Project was downloaded from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6996194/ 

The OTU table was filtered to remove plant samples (Kingdom Plantae), and this table is available here at <b>data/input/otutable.txt</b>. The OTU table was further filtered to remove OTUs with <10 total counts across samples, and OTUs occurring in <2 samples.

### Metadata collection

For each sequenced species in our dataset, we added metadata for body mass and maximum longevity, if available. Body mass data was collected from the Pantheria archives (http://esapubs.org/archive/ecol/E090/184/), the Caviede Vidal dataset (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3689912/), and the Encyclopedia of Life (https://eol.org/). Body mass data was categorized to create three equally-sized groups (excluding Homo Sapiens): big (> 58.7 kg), medium (>19.57 kg, <= 58.7 kg), and small(<= 19.57 kg). Maximum longevity data was obtained from AnAge (http://genomics.senescence.info/species/). The merged metadata table is available here at <b>data/input/EMPmetadata_animal.csv</b>.

### Unsupervised learning analysis
To explore distinct microbial composition structures across samples, an unsupervised cluster analysis was performed on the processed OTU table. OTUs present in less than 5% samples were discarded to obtain robust clusters. Sample-wise distance matrix was then computed using Jensen-Shannon distance on the OTU table of relative abundance. The PAM (partition around medoids) clustering analysis was completed using the cluster package in R software (doi:10.1038/nature09944). The optimal number of clusters was determined to maximize the Silhouette coefficient (doi: 10.1016/0377-0427(87)90125-7). To visualize results of the cluster analysis, principal component analysis was completed using ade4 package in R software. Individual samples were depicted on the space of top two principal components. 

Tutorial for this approach is available at: https://enterotype.embl.de/enterotypes.html. Our R markdown file is also available here at <b>analysis/PAM_with_JSD_2020-02-21_v02.Rmd</b>/


### ANOVA F-test and correlation analysis
For feature selection, ANOVA F-tests were used to identify quantitative metadata variables with significant means differences between clusters. The tutorial for this approach is available at: https://towardsdatascience.com/anova-for-feature-selection-in-machine-learning-d9305e228476/. 

Pearson correlation analysis was performed to evaluate the linear relationships between quantitative metadata variables and an alpha diversity metric (whole tree PD) within each cluster. A step-by-step walkthrough of the ANOVA and correlation analyses is available at <b>analysis/Methods_ANOVA_correlations.pdf</b> and the python codes for these analyses are available at <b>analysis/Internal_Microbime_Analyses.ipynb</b>.
 

