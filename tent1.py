def dat455():
    labbs = input("Vilka labbar har du gjort? ")
    labbs.split(",")
    if "1" and "2" and "3" in labbs:
        tenta = input("Hur många poäng fick du i tentan? ")
        if int(tenta) > 15:
            print("Grattis, du har klarat kursen!")
        else:
            print("Du har inte klarat kursen ännu, men du kan komma till omtentan.")
    else:
        print("Tyvärr kan du inte klara kursen den här gången.")
    





dat455()