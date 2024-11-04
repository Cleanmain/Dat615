import sys


def tokenize(filename):
    file = open(filename, encoding="utf-8")
    lines = file.readlines()
    words = []
    for line in lines:
        start = 0
        end = 0
        while start < len(line):
            while start < len(line) and line[start].isspace():
                start = start + 1
            if start >= len(line):
                break
            elif line[start].isalpha():
                end = start
                while end < len(line) and line[end].isalpha():
                    end = end + 1
                word = line[start:end]
                #print(word.lower()+ " Is a word")
                words.append(word.lower())
                start = end
            elif line[start].isdigit():
                end = start
                while end < len(line) and line[end].isdigit():
                    end = end + 1
                number = line[start:end]
                #print(number + " Is a number")
                words.append(number)
                start = end
            else:
                end = start
                symbol = line[start:end + 1]
                #print(symbol + " Is a symbol")
                words.append(symbol)
                start = start + 1
    print(words)
    return words


def countWords(words, stopWords):
    dictonary = {}
    start = 0
    index = 0
    for word in words:
        while index < len(words):
            if len(stopWords) <= index:
                #print("This word/symbol/number         " + words[start] + "                    is not excluded")
                if word not in dictonary.keys():
                    dictonary[word] = 1
                else:
                    dictonary[word] = dictonary.get(word) + 1
                start = start + 1
                index = 0
                break
            elif words[start] == stopWords[index]:
                start = start + 1 
                #print("This word/symbol/number        " + stopWords[index] + "                 is in stopword so excluded")
                index = 0
                break
            elif len(stopWords) > index:
                index = index + 1
    print(dictonary)
    return dictonary

def printTopMost(frequencies,n):
    index = 0
    sort = sorted(frequencies.items(), key=lambda items: -items[1])
    while index < n:
        Currentvalue = str(sort[index][1])
        Currentkey = sort[index][0]
        print(Currentkey.ljust(20)   + Currentvalue.rjust(20)) 
        index = index + 1

def readstopwords():
    mystopwords = []
    DelWords1 = open("eng_stopWords.txt" , encoding="utf-8") 
    for word in DelWords1:
        yo = word.strip("\n")
        mystopwords.append(yo)
    return mystopwords

def testar(words,Stopwords):
    dictionary = {}
    for word in words:
        if word in Stopwords:
            print("är med" + word)
        else:
            if word not in dictonary.keys():
                    dictonary[word] = 1
            else:
                dictonary[word] = dictonary.get(word) + 1

words = tokenize("article1.txt")
mystopwords = readstopwords()

dict = countWords(words, mystopwords)
printTopMost(dict,20)
testar(words,mystopwords)