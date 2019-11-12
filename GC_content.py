#Write a script with a function that will calculate the GC content for a DNA sequence
#Create a random DNA sequence that is 5,000 bp long (STRING, no spaces, no commas)
#Break the sequence into smaller sequences 100 bp long
#In a loop, use the GC function you created to calculate the GC content for each smaller sequence
#As a reminder, GC content is the G + C/total bp
#Argparse the length of the original DNA sequence and the length of the short sequences


# imort needed modules
import random
import argparse

#	Set up arguments to get from user
ap = argparse.ArgumentParser()
ap.add_argument("-l", "--seqlength", required=True, type= int, help="length of random DNA sequence to be generated")
ap.add_argument("-f", "--fragsize", required=True, type= int, help="size of fragments the random sequence will be broken into")
args=vars(ap.parse_args())

# Assign all arguments to the variables that will be used in the script
SEQ_LEN=args["seqlength"]
FRAG_SZ=args["fragsize"]

# create a list of bases to randomly choose from
bases = ["A", "C", "T", "G"]

# make a string of random bases of length set by user
# here the .join command joins the list output from random.choices into an empty string
sequence = ''.join(random.choices(bases, k=SEQ_LEN))

# split the dna sequence into smaller fragments (frag size supplied by user)
shorties=[sequence[i:i+FRAG_SZ] for i in range(0, SEQ_LEN, FRAG_SZ)]
print(shorties)

def gc_content(DNAseq):
	"""calculates GC content in a DNA sequence"""
	C=sequence.count("C")
	G=sequence.count("G")
	GC=(G+C)/SEQ_LEN
	return GC
	
for seq in shorties:
	G_C=gc_content(seq)
	print(seq, "contains", G_C, "percent G's and C's")
	
	
	
