import collections
Nucleotides=["A","C","G","T"]
# Write a function to validate the Nucleotide
def ValidateSeq(dna_seq):
    tempseq=dna_seq.upper()
    for nu in tempseq:
        if nu not in Nucleotides:
            return False
    return tempseq

# This function count nucleotide frequency
def countNucFrequency(seq):
    tempFreqDict={"A":0,"C":0,"G":0,"T":0}
    for nu in seq:
        tempFreqDict[nu]+=1
    return tempFreqDict,dict(collections.Counter(seq))
