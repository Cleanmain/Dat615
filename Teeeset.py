def substantiv():
    words = input("ange substantiv: ")
    words = words.split()
    for word in words:
        answer = []
        i = 0
        if ord[(len(ord)-1):] == "a":
            word = ord[:-1]
            while i < 4:
                if i == 0:
                    answer.append(ord)
                    i = i + 1
                elif i == 1:
                    answer.append(word + "an")
                    i = i + 1
                elif i == 2:
                    answer.append(word + "or")
                    i = i + 1
                else:
                    answer.append(word + "orna")
                    i = i + 1
                
        elif ord[(len(ord)-3):] == "ion":
            word = ord[:-3]
            while i < 4:
                if i == 0:
                    answer.append(ord)
                    i = i + 1
                elif i == 1:
                    answer.append(word + "tionen")
                    i = i + 1
                elif i == 2:
                    answer.append(word + "tioner")
                    i = i + 1
                else:
                    answer.append(word + "tionerna")
                    i = i + 1
        elif ord[(len(ord)-3):] == "are":
            word = ord[:-3]
            while i < 4:
                if i == 0:
                    answer.append(ord)
                    i = i + 1
                elif i == 1:
                    answer.append(word + "aren")
                    i = i + 1
                elif i == 2:
                    answer.append(word + "are")
                    i = i + 1
                else:
                    answer.append(word + "arna")
                    i = i + 1
        elif ord[(len(ord)-1):] == "e":
            word = ord[:-1]
            while i < 4:
                if i == 0:
                    answer.append(ord)
                    i = i + 1
                elif i == 1:
                    answer.append(word + "et")
                    i = i + 1
                elif i == 2:
                    answer.append(word + "en")
                    i = i + 1
                else:
                    answer.append(word + "ena")
                    i = i + 1
        else:
            while i < 4:
                if i == 0:
                    answer.append(ord)
                    i = i + 1
                elif i == 1:
                    answer.append(ord + "en")
                    i = i + 1
                elif i == 2:
                    answer.append(ord + "ar")
                    i = i + 1
                else:
                    answer.append(ord + "arna")
                    i = i + 1
        print(answer)

substantiv()