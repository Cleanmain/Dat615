def code_words(text, dictionary):
    words = text.split()
    sentence = ""
    for word in words:
        if word not in dictionary.keys():
            sentence = sentence +  word + " "
        else:
            sentence = sentence + dictionary[word] + " "
    
    print(sentence)





d = {"happiness": "cake", "homework": "date"}
code_words("you have your happiness",d)