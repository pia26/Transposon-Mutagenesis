#import numpy as np
import operator
import argparse

#parser = argparse.ArgumentParser(description='Find the most repeating subsequences in a DNA sequence')
#parser.add_argument('FILENAME', metavar='N', type=str, help='The name of the .fna file to process')
#parser.add_argument('--len', type=int, default=10, help='The length of the sequence')
#parser.add_argument('--n_out', type=int, default=20, help='The number of subsequences to output')
#parser.add_argument('--OUTFILE', type=str, default=None, help='The optional output file')
#args = parser.parse_args()

#fname= args.FILENAME
#length=args.len
#n_out=args.n_out
#outfile=args.OUTFILE

#seq=np.loadtxt('NC_009848.fna',dtype=str,comments='\n',skiprows=1)
#file=open(fname,'r')
#seq=file.read()
#seq=seq.split('\n',1)[-1]
#seq=seq.replace('\n','')

#no more np 
fname = "copy.txt"
fobj = open(fname)
seq = fobj.read()
fobj.close()

from collections import Counter
length=13
freq = Counter()

for i in range(len(seq) - length):
        print("aaa")
        freq[seq[i:i+length]] += 1

print (freq.most_common(10))

#if outfile!=None:
#	np.savetxt(outfile, np.array(primers[:n_out]), fmt='%s', delimiter='\t')
