#WARNING: only use this program if you wish to conduct a visual alignment for every sequence pair at once
#This program may take time to finish running
#This program will likely utilize a lot of processing power to finish
#Using an output file for this program is strongly recommended, as real-time processing may crash the terminal
#A .txt output file is recommended

from Bio import AlignIO, pairwise2

sto_file = r"C:\Users\Tania\Documents\Bioinformatics\Protein Bioinformatics\Pr Bio Labs\Neur_chan_memb.alignment.seed\Neur_chan_memb_SEED.sth"
output_file = r"C:\Users\Tania\Documents\Bio notepad reads\ncm_pairwise_alignments.txt"

alignment = AlignIO.read(sto_file, "stockholm")

with open(output_file, "w") as outfile:
    for i in range(len(alignment)):
        for j in range(i + 1, len(alignment)):
            seq1 = str(alignment[i].seq)
            seq2 = str(alignment[j].seq)

            alignments = pairwise2.align.globalxx(seq1, seq2)

            for aligned_pair in alignments:
                outfile.write(f"Pairwise alignment between sequences {i+1} and {j+1}:\n")
                outfile.write(pairwise2.format_alignment(*aligned_pair))
                outfile.write("\n")

