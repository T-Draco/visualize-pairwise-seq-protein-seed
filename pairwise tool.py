from Bio import AlignIO, pairwise2

sto_file = r"C:\Users\Tania\Documents\Bioinformatics\Protein Bioinformatics\Pr Bio Labs\Cystatin_Legumain_Seed\Pep_C13.seed\PC13_SEED.ann"

alignment = AlignIO.read(r"C:\Users\Tania\Documents\Bioinformatics\Protein Bioinformatics\Pr Bio Labs\Cystatin_Legumain_Seed\Pep_C13.seed\PC13_SEED.ann", "stockholm")

seq1 = alignment[0].seq
seq2 = alignment[1].seq

alignments = pairwise2.align.globalxx(seq1, seq2)

for alignment in alignments:
    print(pairwise2.format_alignment(*alignment))