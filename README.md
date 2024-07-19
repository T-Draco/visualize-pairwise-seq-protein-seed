# visual-pairwise-seq-protein-seed
Protein "SEED" sequences are representative sequences of each protein from a specific family. Pairwise and multisequence alignments can be used to analyze sequence similarities between different proteins within the same family.  Biopython was used. This tool visualizes sequence alignments. PLEASE NOTE: I am an amateur programmer, and this is my first post on github. Currently, the code may have issues with repeated pairwise sequencing. 

For a visual tutorial, please open the "Pairwise_alignment_Visualizing_VS_code_Tutorial.pdf" file. 

# Using the program
1. Select the Pfam entry of your protein of interest. Go to the “Alignment” tab, and from “Available alignments” select the “seed” alignment. Download the seed alignment in clustal2 format.
2. To find the pairwise sequence alignment between 2 homologous sequences of the neurotransmitter membrane channel, a stockholm file from Pfam was input into a biopython code using the pairwise 2 package. This step was repeated with 2 homologous sequences of the protein of interest: Peptidase C13. This was also done using a stockholm file of the protein of interest found on Pfam. 
