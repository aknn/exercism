def to_rna(dna_strand):
    transcription_map = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    rna_strand = ""
    for nucleotide in dna_strand:
        rna_strand += transcription_map[nucleotide]
    return rna_strand