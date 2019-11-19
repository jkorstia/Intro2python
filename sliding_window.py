# Write a function to create sliding windows along dna sequences
# within each window, calculate GC content using the function you wrote last week
# plot results as a histogram using matplotlib
# Use argparse

# imort needed modules
from Bio import SeqIO
import argparse

#	Set up arguments to get from user
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_fasta", required=True, help="input fasta file")
ap.add_argument("-w", "--window_size", required=True, type= int, help="size of sliding windows")
args=vars(ap.parse_args())

# Assign all arguments to the variables that will be used in the script
FASTA=args["input_fasta"]
WIN_SZ=args["window_size"]

# read in fasta file
for record in SeqIO.parse(FASTA, "fasta"):
	record.seq
shorties=[sequence[i:i+FRAG_SZ] for i in range(0, SEQ_LEN, FRAG_SZ)]

def gc_content(DNAseq):
	"""calculates GC content in a DNA sequence"""
	C=sequence.count("C")
	G=sequence.count("G")
	GC=(G+C)/SEQ_LEN
	return GC
	
for seq in shorties:
	G_C=gc_content(seq)
	print(seq, "contains", G_C, "percent G's and C's")
