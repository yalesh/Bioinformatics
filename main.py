# DNA Toolset/Code testing file
from DNA import *
import random
randDNAStr= ''.join([random.choice(Nucleotides)for nu in range(50)])

#randomStr = "ATTatttc"
DNAStr=ValidateSeq(randDNAStr)
#print(ValidateSeq(randDNAStr))
print(countNucFrequency(DNAStr))

