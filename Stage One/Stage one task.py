#Task 1: DNA TRanslation:
Task1: #Function 1: Write a function for translating DNA to protein
def translate_dna (dna_seq):
#Transcribe DNA to RNA
    rna_sequence = ""
    for bases in dna_seq:
        if bases == "A":
            rna_sequence = rna_sequence + "U"
        elif bases == "T":
            rna_sequence = rna_sequence + "A"
        elif bases == "G":
            rna_sequence = rna_sequence + "C"
        elif bases == "C":
            rna_sequence = rna_sequence + "G"
        else:
            print("DNA sequence contains an inappropriate nucleotide")
            quit()
#Translate RNA to protein
    protein_sequence = ""
    codon_table = {
            'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
            'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
            'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*', 'UGA': '*',
            'UGU': 'C', 'UGC': 'C', 'UGG': 'W',
            'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
            'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
            'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'ACU': 'T', 'ACC': 'T',
            'ACA': 'T', 'ACG': 'T', 'AAU': 'N', 'AAC': 'N',
            'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S',
            'AGA': 'R', 'AGG': 'R', 'GUU': 'V', 'GUC': 'V',
            'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A',
            'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 'GAC': 'D',
            'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G',
            'GGA': 'G', 'GGG': 'G'
        }
    #find startcodon
    start_codon = rna_sequence.find("AUG")
    #Start translation
    for codons in range(start_codon, len(rna_sequence)- len(rna_sequence)%3, 3):
        codon = rna_sequence[codons:codons + 3]
        aminoacid = codon_table.get(codon)
        if aminoacid == "*":
            break
       else:
            protein_sequence += aminoacid
    print(f"The result of the translation of the DNA sequence: {dna_seq} to protein is {protein_sequence}")
dna_sequence = "ATTACTGCTACTAGCCCTTAATCGGACGAC"
protein_seq = translate_dna(dna_sequence)

#Task2: Generate logistic curve
#Nt = K / (1 + (2.71828**(-r*t)))where Nt is the population size at generation (time) t, K is the carrying capacity, r is the growth rate and t is the generation(time)
def logistic_curve(Nt, cycle, r=0.2, K = 1000, lag_range= 5, exp_range = 15):#lag_range and exp_range are random values to simulate the number of generations fpr the lag phase and exponential phase respectively
    population_size = {}
    for cycles in range (1, cycle+1):#"cycle + 1" is to meet the actual generation time, cycles is the same as time or generation
        if cycles <= lag_range:# The first five generations should represent the lag phase, where populatioon size (N) is more or less constant as microbes are getting adapted to their environment
            logistic_growth = Nt
            population_size.update({cycles : logistic_growth})
        elif cycles > lag_range and cycles <= exp_range and logistic_growth < 600:#The next seven generations  represent the exponential (log) phase. Another criteria for exponential growth is that population size (N) should be less than the carrying capacity at a value of 600
            exp_growth = Nt * 2.71828**(r*cycles)# 2.718282 is the value for "e"
            #Check if the exponential growth is greater than 80% of the carrying capacity (800). If it is, use the logistic formula. If not, calculate the exponential phase using the exponential formula
            if exp_growth > 800:
                logistic_growth = K / (1 + (2.71828**(-r*cycles)))
                population_size.update({cycles : logistic_growth})
            else:
                logistic_growth = exp_growth
                population_size.update({cycles : logistic_growth})
        elif cycles > exp_range and logistic_growth <= 800:# if after 12 generations, the population size is way below the carrying capacity at an estimated figure of less than 800, continue in the exponential phase. If not, move to the stationary phase
            exp_growth = Nt * 2.71828**(r*cycles)
            #Check if value is greater than carrying capacity. If it is, use the logistic formula. If not, calculate the exponential phase using the exponential formula
            if exp_growth > K:
                logistic_growth = K / (1 + (2.71828**(-r*cycles)))
                population_size.update({cycles : logistic_growth})
            else:
                logistic_growth = exp_growth
                population_size.update({cycles : logistic_growth})
        elif cycles > exp_range and logistic_growth > 800:#If the population size is close to the carrying capacity, i.e greater than 800, use the logistic growth model to simulate the stationary phase
            logistic_growth = K / (1 + (2.71828**(-r*cycles)))
            if logistic_growth >= K:#If a value is more than or equal to the carrying capacity, end the code
                print(f"For generation {cycles}, the population size is {logistic_growth} which is equal to the carrying capacity 'K' of the population\n\n")
                break
            else:
                population_size.update({cycles : logistic_growth})
    print(f"The Generation time : Population size is given as {population_size}")
    return Nt
    return r
    return K
    return logistic_growth
example = logistic_curve(50, 500)

#Task 3: Determine time to reach carrying capacity
def time_to_reach_K(Nt, cycle, r=0.2, K = 1000, lag_range= 5, exp_range = 15):#lag_range and exp_range are random values to simulate the number of generations fpr the lag phase and exponential phase respectively
    for cycles in range (1, cycle+1):#"cycle + 1" is to meet the actual generation time, cycles is the same as time or generation
        if cycles <= lag_range:# The first five generations should represent the lag phase, where populatioon size (N) is more or less constant as microbes are getting adapted to their environment
            logistic_growth = Nt
        elif cycles > lag_range and cycles <= exp_range and logistic_growth < 600:#The next seven generations  represent the exponential (log) phase. Another criteria for exponential growth is that population size (N) should be less than the carrying capacity at a value of 600
            exp_growth = Nt * 2.71828**(r*cycles)# 2.718282 is the value for "e"
            #Check if the exponential growth is greater than 80% of the carrying capacity (800). If it is, use the logistic formula. If not, calculate the exponential phase using the exponential formula
            if exp_growth > 800:
                logistic_growth = K / (1 + (2.71828**(-r*cycles)))
            else:
                logistic_growth = exp_growth
        elif cycles > exp_range and logistic_growth <= 800:# if after 12 generations, the population size is way below the carrying capacity at an estimated figure of less than 800, continue in the exponential phase. If not, move to the stationary phase
            exp_growth = Nt * 2.71828**(r*cycles)
            #Check if value is greater than carrying capacity. If it is, use the logistic formula. If not, calculate the exponential phase using the exponential formula
            if exp_growth > K:
                logistic_growth = K / (1 + (2.71828**(-r*cycles)))
            else:
                logistic_growth = exp_growth
        elif cycles > exp_range and logistic_growth > 800:#If the population size is close to the carrying capacity, i.e greater than 800, use the logistic growth model to simulate the stationary phase
            logistic_growth = K / (1 + (2.71828**(-r*cycles)))
            if logistic_growth >= K:#If a value is more than or equal to the carrying capacity, end the code
                print(f"The Generation time to reach the carrying capacity, 'K' is {cycles} generations")
                break
            else:
                continue
    return Nt
    return r
    return K
    return logistic_growth
example = time_to_reach_K(50, 500)

#Task 4: Hamming distance
def pad_strings(str1, str2):
    max_length = max(len(str1), len(str2))
    str1 = str1.ljust(max_length, "_")
    str2 = str2.ljust(max_length, "_")
    return str1, str2
def calculate_hamming(str1, str2):
    distance = sum(1 for a, b in zip(str1, str2) if a != b)
    return distance
def print_comparison(str1, str2):
    print("Comparing:")
    print(str1)
    print(str2)
    print()
def hamming_distance(str1, str2):
    str1, str2 = pad_strings(str1, str2)
    print_comparison(str1, str2)
    distance = calculate_hamming(str1, str2)
    print(f"Hamming Distance: {distance}")
    return distance
hamming_distance("Valerie", "iamveemartins")
