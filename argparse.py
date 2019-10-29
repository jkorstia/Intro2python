#		Intro2Python Argparse homework
#	1.  Use avan_rm.bed file in my /lustre/work/jenjense/pandas
#	2.  Make sure it has proper column names
#	3.  Determine what Families are in there (SINE, etc)
#	4.  Create new dataframe from that file using only elements in family "SINE" 
#	5.  Drop columns "Strand" and "Score"
#	6.  Create new column "Length"
#	7.  Create new column "Proportion" = Length/Genome size
#	8.  Save dataframe as new csv file "aVan.csv"

####################################################################################

import pandas as pd
import argparse

#	Set up arguments to get from user
ap = argparse.ArgumentParser()
ap.add_argument("-b", "--bedfile", required=True, help="name of repeatmasker bedfile. File must be in pwd")
ap.add_argument("-g", "--genomesize", required=True, type= int, help="size of genome in bp")
ap.add_argument("-f", "--family", required=True, help="TE family to retain")
ap.add_argument("-t", "--taxon", required=True, help="taxon of interest")
args=vars(ap.parse_args())

# Assign all arguments to the variables that will be used in the script
BED=args["bedfile"]
GENOMESIZE=args["genomesize"]
FAMILY=args["family"]
TAXON=args["taxon"]

# 1. read in tab separated bed file
bed=pd.read_csv(BED, sep="\t")

# 2. create a list with column names
fields=["Scaffold", "Start", "Stop", "Element",	"Score", "Strand", "Class", "Family", "Divergence"]
# assign names to columns
bed.columns = fields
# check that column naming was successful
print(bed.head())

# 3. determine how many Classes of TEs there are in the bed file
classes = bed.Class.unique()

# 4. make a new dataframe of only the family specified by the user
keep=bed[bed.Class == FAMILY] 

# 5. drop Strand and Score columns
keep=keep.drop(["Strand", "Score"], axis=1)

# 6. Create Length column and populate with correct values (stop-start)
keep["Length"]=(keep["Stop"] - keep["Start"])

# 7.  Create new column "Proportion" = Length/Genome size
keep["Proportion"]=(keep["Length"] / GENOMESIZE)

# 8. Save dataframe as new csv file "aVan.csv"
export_csv = keep.to_csv(TAXON+'.csv', index=False, header=True)


