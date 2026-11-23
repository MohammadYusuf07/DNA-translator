genetic_code = {
    'UUU': 'Phe', 'UUC': 'Phe',
    'UUA': 'Leu', 'UUG': 'Leu',
    'UCU': 'Ser', 'UCC': 'Ser',
    'UAU': 'Tyr', 'UAC': 'Tyr',
    'UGU': 'Cys', 'UGC': 'Cys',
    'UGG': 'Trp',
    'CUU': 'Leu', 'CUC': 'Leu',
    'AUU': 'Ile', 'AUC': 'Ile',
    'AUA': 'Ile', 'AUG': 'Met',
    'GUU': 'Val', 'GUC': 'Val',
    'GUA': 'Val', 'GUG': 'Val',
    'GCU': 'Ala', 'GCC': 'Ala',
    'GCA': 'Ala', 'GCG': 'Ala',
    'CCU': 'Pro', 'CCC': 'Pro',
    'CCA': 'Pro', 'CCG': 'Pro',
    'ACU': 'Thr', 'ACC': 'Thr',
    'ACA': 'Thr', 'ACG': 'Thr',
    'GCU': 'Ala', 'GCC': 'Ala',
    'GAU': 'Asp', 'GAC': 'Asp',
    'GAA': 'Glu', 'GAG': 'Glu',
    'UGA': 'STOP', 'UAA': 'STOP',
    'UAG': 'STOP',
    'CAU': 'His', 'CAC': 'His',
    'CAA': 'Gln', 'CAG': 'Gln',
    'CGU': 'Arg', 'CGC': 'Arg',
    'CGA': 'Arg', 'CGG': 'Arg',
    'AGU': 'Ser', 'AGC': 'Ser',
    'AGA': 'Arg', 'AGG': 'Arg',
    'GGU': 'Gly', 'GGC': 'Gly',
    'GGA': 'Gly', 'GGG': 'Gly'

}

# Input DNA sequence
dna = input("Enter DNA sequence: ").upper().strip()


#validate dna 
if not dna or any(base not in "ATGC" for base in dna):
    print("Invalid DNA sequence!")

else:
        # Transcription
    mrna = dna.replace("T", "U")

    print("\nDNA:", dna)
    print("mRNA:", mrna)

    # Divide into codons
    codons = [mrna[i:i+3] for i in range(0, len(mrna)-2, 3)]

    print("\nCodons:", codons)

    # Translation
    protein = []
    start_found = False

    for codon in codons:
        if codon == "AUG":
            start_found = True

        if start_found:
            amino = genetic_code.get(codon , "unknown")

            if amino == "STOP":
                print("Stop codon found:", codon)
                break

            protein.append(amino)

    if start_found:
        print("Protein:", "-".join(protein))
    else:
        print("No start codon found!")



