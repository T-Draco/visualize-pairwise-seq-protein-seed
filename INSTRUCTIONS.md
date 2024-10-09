# visual-pairwise-seq-protein-seed
Protein "SEED" sequences are representative sequences of each protein from a specific family. Pairwise and multisequence alignments can be used to analyze sequence similarities between different proteins within the same family.  Biopython was used. This tool visualizes sequence alignments. 

For single pairwise sequence alignments, please use "pairwise_tool.py"

PLEASE NOTE: I am an amateur programmer, and this is my first post on github. Currently, the 2nd code "Full_pairwise_alignment_sequencing_tool.py" (3rd step) may have issues with repeated pairwise sequencing. Please read all warnings for this program, as it requires a lot of processing power and about 3 GB of memory depending on the .seed or .ann file. 
For a visual tutorial, please open the "TUTORIAL_pairwise_alignment_visualizing_tool.pdf" file. 

Biopython download page: README.rst
Please read LICENSE.rst

# Using the program
1. Select the Pfam entry of your protein of interest. Go to the “Alignment” tab, and from “Available alignments” select the “seed” alignment. Download the seed alignment in clustal2 format. The folder will likely be labelled .seed, however .ann files work with this program as well. 
2. To find the pairwise sequence alignment between 2 homologous sequences of your protein of interest, input your Pfam stockholm/clustal2 file into the Biopython pairwise package "pairwise_tool.py". This step can be repeated with different sequences of the protein of interest by editing the "alignment[0]" number. 
3. WARNING: This code requires a lot of processing power. You can use the "Full_pairwise_alignment_sequencing_tool.py" code to conduct a sequence alignment between each sequence in the .seed file; however, this will take up a good bit of memory, a lot of computer processing power, and it may even crash your terminal. Running the code on a terminal may give you a bunch of random numbers; however, you can simply exit the terminal, and you should still have some, if not all pairwise sequences, analyzed on the output .txt file.

Copyright: This program utilizes Biopython, which is considered a free use package. This program is available for free use, and it was created for entirely non-profit reasons. 
