# Task 1 of 4
# Function to translate DNA to protein
translate_dna <- function(dna_sequence) {
  genetic_code <- c(
    TTT="F", TTC="F", TTA="L", TTG="L", CTT="L", CTC="L", CTA="L", CTG="L",
    ATT="I", ATC="I", ATA="I", ATG="M", GTT="V", GTC="V", GTA="V", GTG="V",
    TCT="S", TCC="S", TCA="S", TCG="S", CCT="P", CCC="P", CCA="P", CCG="P",
    ACT="T", ACC="T", ACA="T", ACG="T", GCT="A", GCC="A", GCA="A", GCG="A",
    TAT="Y", TAC="Y", TAA="*", TAG="*", CAT="H", CAC="H", CAA="Q", CAG="Q",
    AAT="N", AAC="N", AAA="K", AAG="K", GAT="D", GAC="D", GAA="E", GAG="E",
    TGT="C", TGC="C", TGA="*", TGG="W", CGT="R", CGC="R", CGA="R", CGG="R",
    AGT="S", AGC="S", AGA="R", AGG="R", GGT="G", GGC="G", GGA="G", GGG="G"
  )
  # Split the DNA sequence into codons for amino-acids
  codons <- substring(dna_sequence, seq(1, nchar(dna_sequence)-2, by=3), seq(3, nchar(dna_sequence), by=3))
  protein <- paste(genetic_code[codons], collapse="")
  return(protein)
}
#team serine protein sequence
dna_sequence <- "ACGGAGGCTATGTAGAGTGAACGGATTAACGAGTAA"
protein <- translate_dna(dna_sequence)
print(protein) # should print "TEAM*SERINE*"
