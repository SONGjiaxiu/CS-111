
#def mean(list):
#    sum = 0
#    for index in range (len(list)):
#        sum=sum+list[index]
#    return sum/len(list)


#def main():
    #codons = ["AAA", "ATG", "GTA", "CGA", "CCG", "ATG", "GTA", "CCC"]



'''dictionary:
     Key          Values             Example
    codon        frequency       {"AAA":1, "GTA":2}
   student        house      house={"Harry","Gryffindor","Draco","Slytherin"}
'''

def frequency(list):
    freq={}
    for index in range(len(list)):
        codon = list[index]
        if codon not in freq:            #insert into dictionary
            freq[codon] = 1
        else:
            freq[codon] = freq[codon] +1  #update dictionary
    return freq
    

def mode(list):
    freq = frequency(list)
    maxValue = max(freq.values())

    answer = []
    for key in freq:
        if freq[key] == maxValue:
            answer.append(key)
    return answer


def main():
   # print(mean([1,2,3]))
    codons = ["AAA", "ATG", "GTA", "CGA", "CCG", "ATG", "GTA", "CCC"]
    freq = frequency(codons)

   #iterate through dictionary
    #for key in freq:
 #       print(key, "appears", freq[key], "times")

    print(mode(codons))

main()
