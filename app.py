# code by Henrik und Philipp



# coding: UTF-8



# - moduls
from nltk.tokenize import sent_tokenize



# - Eingabe :



# - Ausgabe :


# - Verarbeitung des Textes


# Test :
#test = "@?\`:;,.-_'#%&$§^"
#print(test.upper())
#print(test.lower())

#testtext1 = "HAllo ß"
#testtext2 = "ich will was essen"
#test2text1 = "essen Nahrung usw"

#print(testtext1.lower()) # --> "hallo ß"
#print(testtext1.upper()) # --> "HALLO SS"
#testtext1.replace("ß","ss") # essen --> essen

#print(testtext2.lower()) # --> "hallo ss"
#print(testtext2.upper()) # --> "HALLO SS"

#testtext2.replace("ss","ß") # ich will was eßen

# -


# - Gefühle
gefuelsehrschlecht = 0
gefuelschlecht = 1
gefuelnormal = 3
gefuelgut = 4
gefuelsehrgut = 5


# - Neue/n begriff erklären
erklneuenbegriff = "Ich erklär dir einen nuen begriff"


# - Name des Sprachassistenten
assistentsname = "clana"


# - Letzte Nachicht :
letztenachicht = ""


# - START
while True:
    # Eingabe :
    input1 = input(" Eingabe : ")


    # - Verarbeitung des Textes
    input1 = input1.lower()
    listinput1 = input1.split()
    sendtokeninput1 = sent_tokenize(input1) #probieren! pip install nltk
    print(sendtokeninput1) # --
    leninput1 = len(input1)
    lenlistinput1 = len(listinput1)

    # - if hallo
    if lenlistinput1 > 0:
        if listinput1[0] == "hi" or "hallo" or "hey":
            if lenlistinput1 > 1:
                if listinput1[1] == assistentsname:
                    print("!!Ich bin gemeint!!")

            print("abc")
        if listinput1[0] == "guten":
            print("test1")
            if lenlistinput1 > 1:
                if listinput1[1] == "morgen" or "vormittag" or "mittag" or "abend":
                    if lenlistinput1 > 2:
                        if listinput1[2] == assistentsname:
                            print("!!Ich bin gemeint!!")
                        else:
                            print("")
    else:
        print("- Error : keine Eingabe Daten !!")
            

    # Neue/n begriff erklären
    if "Ich erklär dir ein neues wort" or "Ich erklär dir einen nueen begriff" == "x":
        print("xx")
