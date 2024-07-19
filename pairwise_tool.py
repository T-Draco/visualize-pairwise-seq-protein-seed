from Bio import AlignIO, pairwise2

sto_file = r"" #Insert your .seed stockholm/clustal2 filepath here ""

alignment = AlignIO.read(r"", "stockholm") #Insert your .seed stockholm/clustal2 filepath again ""

seq1 = alignment[0].seq
seq2 = alignment[1].seq

alignments = pairwise2.align.globalxx(seq1, seq2)

for alignment in alignments:
    print(pairwise2.format_alignment(*alignment))