import random
import csv
from collections import Counter

with open("data.txt", newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    data =[]
    for row in rows:
        data.append(row)
#************************* THIS SECTION (1) DEALS WITH VARIOUS LISTS THAT MAY BE USEFUL IN THE MAKING OF THIS PROGRAM **************************

#Making a list of 0th elements
listof0s = []
len(data)
for i in range(len(data)):
    x = data[i][0]
    listof0s.append(x)

#Made a single list of each element in each list.
listofall = []
for i in range(len(data)):
    x = data[i]
    listofall.extend(x)

#Trying to make a list of all Origins
listoforigins = []
listofnotorigins = []
listofnot0s = []
#Made a list of all elements which are not 0th elements in order to make a list of Origins
listofnot0s = list((Counter(listofall)-Counter(listof0s)).elements())
for i in range(len(listof0s)):
    x = listof0s[i]
    if x in listofnot0s:
        listofnotorigins.append(x)
listoforigins = list((Counter(listof0s)-Counter(listofnotorigins)).elements())

#Accidentaly made a list of endpoints[note that the below method subtracts all elements unlike the Counter method which subtracts only one element per element]
listofendpoints = list(set(listofall) - set(listof0s))

#printing all the created lists to see if it works
# print("\nList of NOT ORIGINS:\n")
# print(listofnotorigins)
# print("\nList of ZEROS:\n")
# print(listof0s)
# print("\nList of Origins\n")
# print(listoforigins)

#************************* END OF SECTION (1) **************************
#************************* THIS SECTION (2) DEALS WITH CREATING FUNCTIONS **************************
#Scoring system
score = 0

#Main Function borrowed from V1 (for the most part)
def main(answer):
    global score
    nestedlist = []
    if answer in listof0s:
        print("********************************************\n")
        print("What comes after "+answer+" ?\n")
        print("Select the correct concept in the series:\n")
        #Correct option:
        for i in range(len(data)):
            if answer == data[i][0]:
                for x in range (len(data[i])):
                    nestedlist.append(data[i][x])
        nestedlist.pop(0)           
        correctoption = random.choice(nestedlist)
        #Other options:
        finalotheroptionlist = list(set(listofall) - set(nestedlist))

        option2 = random.choice(finalotheroptionlist)
        option3 = random.choice(finalotheroptionlist)
        option4 = random.choice(finalotheroptionlist)
        option5 = random.choice(finalotheroptionlist)
        optionslist1 = [correctoption, option2, option3, option4, option5]
        random.shuffle(optionslist1)
        #print(optionslist1)
        print(optionslist1[0])
        print(optionslist1[1])
        print(optionslist1[2])
        print(optionslist1[3])
        print(optionslist1[4])
        print("\n")
        
        answer1 = input("INPUT HERE: ")
        if answer1 in nestedlist:
            score = score+5
            print("**********************************************")
            print("CORRECT ANSWER!")
            print("SCORE = "+str(score))
            main(answer1)
        
        else:
            print("*********************************************\n")
            print("WRONG ANSWER")
            score = score-10
            print("SCORE = "+str(score))
            start()

    elif answer in listofendpoints:
        print("END OF LINE\n")
        print("********************************************\n")
        start()
    
    else:
        print("*********************************************\n")
        print("INVALID INPUT")
        print("SCORE = "+str(score))
        start()

#Start Function
def start():
    print("Select any of the following topics or type your own:\n")
    for i in range(5):
        optionelement = random.choice(listoforigins)
        print(optionelement)
    print("\n")
    ans = input("INPUT HERE: ")
    main(ans)

#Executing the Start Function
start()