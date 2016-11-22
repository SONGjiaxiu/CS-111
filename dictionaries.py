

def bonus(salary):
    for key in salary:
        salary[key] = salary[key] * 1.05


def updateAge(list,dic):
    for key in dic:
        word = dic[key]
        if word in list:
            dic[key] = dic[key] + 1
        else:
            dic[key] = dic[key]
    return dic


def first(list):
    answer = {}
    for i in range(len(list)):
        word = list[i]
        letter= word[0]
        if letter in answer:
            answer[letter] = answer[letter]+1
        else:
            answer[letter] = 1
    return answer
    
def histogram(list):
    answer = {}
    for i in range(len(list)):
        word = list[i]
        if word in answer:
            answer[word] = answer[word] + 1
        else:
            answer[word] = 1
    return answer



def main():
    #print(updateAge(["taylor","tyler","alex","paul","aaron"],{"taylor":18,"ryan":17,"tyler":20,"aaron":13,"melissa":12}))
    #print(first(["ant","beaver","cat","dog","armadillo"]))
    print(histogram(["a","b","c","c","d","a"]))

main()
