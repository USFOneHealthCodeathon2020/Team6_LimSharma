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

The OTU table was filtered to remove plant samples (Kingdom Plantae), OTUs with <10 total counts across samples, and OTUs occurring in <2 samples

### Metadata collection

For each sequenced species in our dataset, we added metadata for body mass and maximum longevity, if available. Body mass data was collected from the Pantheria archives (http://esapubs.org/archive/ecol/E090/184/), the Caviede Vidal dataset (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3689912/), and the Encyclopedia of Life (https://eol.org/). Body mass data was categorized into big, medium, and small. Maximum longevity data was obtained from AnAge (http://genomics.senescence.info/species/).

### Unsupervised learning

We used unsupervised learning on the processed OTU table to cluster the samples based on Jensen-Shannon Distances using the
PAM (partition around medoids) algorithm implemented in R.

Tutorial for this approach is available at: https://enterotype.embl.de/enterotypes.html

### Cluster analysis

We analyzed metadata variables that best explains the cluster membership using a PERMANOVA F-test. Pearson correlation was also used to examine correlations between metadata vairables.







