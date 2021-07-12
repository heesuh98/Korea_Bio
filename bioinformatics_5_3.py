codon_dic = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "TAT": "Y",
    "TAC": "Y",
    "TAA": "*",
    "TAG": "*",
    "TGT": "C",
    "TGC": "C",
    "TGA": "*",
    "TGG": "W",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "M",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGT": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}

seq_list = []
fr = open("sequence.nucleotide.fasta", "r")
for line in fr:
    if line[0] != ">":
        line = line.strip()
        seq_list.append(line)
seq = "".join(seq_list)

a_list = []
codon_list = []
aa = []
for a in seq:
    a_list.append(a)
    if len(a_list) % 3 == 0:
        codon = "".join(a_list)
        codon_list.append(codon)
        aa.append(codon_dic[codon])
        a_list = []
        if len(codon_list) % 20 == 0:
            codon_str = "".join(codon_list)
            aa_str = "  ".join(aa)
            print(codon_str)
            print(aa_str)
            codon_list = []
            aa = []
codon_str = "".join(codon_list)
aa_str = "  ".join(aa)
print(codon_str)
print(aa_str)
