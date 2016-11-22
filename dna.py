
def complement(dna):
    '''computes complement of a DNA string
       Input: DNA string
       Output: The String's reverse complement
       '''


    answer=""
    dna=dna.upper()
    for index in range(len(dna)-1,-1,-1):
        nt=dna[index]
        if nt=="G":
            answer = answer + "C"
        elif nt == "T":
            answer = answer + "A"
        elif nt == "A":
            answer = answer + "T"
        else:
            answer = answer + "G"
    return answer




def RNAcomplement(dna):
    
    answer=""
    dna=dna.upper()
    for index in range(len(dna)):
        nt=dna[index]
        if nt =="G":
            answer = answer + "C"
        elif nt == "T":
            answer = answer + "A"
        elif nt == "A":
            answer = answer + "U"
        else:
            answer = answer + "G"
    return answer


def countCodon(dna, codon):
    '''Computes the number of times the codon appears is dna
       Input: DNA string
       Output: the number of occurrences of the codon
       '''
    codon=codon.upper()
    dna=dna.upper()
    answer = 0
    for index in range(len(dna)-2):
        if dna[index:index+3] == codon:
            answer = answer + 1
    return answer




def main():
    print(countCodon("gattacttggattcaggattaattt","att"))

main()
