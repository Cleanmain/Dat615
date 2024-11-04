def duplicates(xs):
    i = 0
    dictionary = {}
    answer = []
    for element in xs:
        if element not in dictionary.keys():
            dictionary[element] = 1
        else:
            dictionary[element] = dictionary.get(element) + 1
    for valuepair in dictionary:
        if dictionary.get(valuepair) > 1:
            answer.append(valuepair)
    print(answer)



            
        




duplicates([1,2,3,2,1,1,5])