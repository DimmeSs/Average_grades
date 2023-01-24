import os
from termcolor import colored
#Text Language -> Polish

#Window size
os.system("mode con: cols=55 lines=20")

def design():
    a = "#" + "="*51 +"#"
    return a
    #definition that returns characters for cmd design
grades = []#a list where the grades entered by the user are kept
weights = []#a list where the weights entered by the user are kept

def Delete_grade():#definition that allows you to select a grades and remove it along with its weight
    print(design())
    print("\nLista ocen:",grades)
    while True:
        nr = input("\nPodaj miejsce oceny, którą chcesz usunąć \n(np. 1 lub 2 itp..) : ")
        if nr == "":
            print(colored("Nie podałeś miejsca. Wpisz ponownie","red"))#colored makes text color => red
        elif len(grades) < int(nr):
            print(colored("Nie ma w tym miejscu oceny","red"))
        else:
            nr = int(nr)
            grades.pop(nr-1)#remove selected grade 
            weights.pop(nr-1)#remove selected weight
            print("Aktualna lista ocen:",grades,"\n")
            break#go back to program

print(design())
next_grade = input("\nJeżeli Chcesz zakończyć -> Wpisz [end]\nJeżeli Chcesz usunąć ocene -> Wpisz [delete]\nJeżeli Chcesz korzystać z programu -> Wciśnij [Enter]\n")#info
if next_grade.lower() == "end":
    exit()
elif next_grade.lower() == "delete":
    print(colored("\nNie ma sensu teraz usuwać nie mając żadnych ocen :3\nPrzypuszczam że chcesz na początku dodać oceny :p","red"))#"that'w what she said"
while True:

    while True:
        print(design())
        grade = input("\nPodaj ocenę : ")#retrieving a grade from the user
        if next_grade.lower() == "end" or grade.lower() == "end": exit()
        elif grade == "" or grade not in ["1", "1+", "2-", "2", "2+", "3-", "3", "3+", "4-", "4", "4+", "5-", "5", "5+", "6-", "6", "6+"]:#Grade can't be < 0.75 and have to be < 7 
            print(colored("Niepoprawna ocena \n(Jeżeli chcesz zakończyć program wpisz [end] )\n","red"))
        else: break  

    while True:     
        weight = input("Podaj wagę oceny : ")#retrieving  grade weight from the user
        try:
            if next_grade.lower() == "end" or grade.lower() == "end" or weight.lower() == "end":exit()
            elif weight == "": 
                print(colored("Nie podałeś wagi oceny \n(Jeżeli chcesz zakończyć program wpisz \"end\"\n","red"))
                print(design())
            else:break
        except AttributeError:
            break

    weight = float(weight)
    
    if '+' in grade:#converting a [+] grade (for example 4+ to float 4+0.50)
        grade = float(grade.replace('+','')) + 0.5
    elif '-' in grade:
        grade = float(grade.replace('-','')) - 0.25
    else:
        grade = float(grade)
        
    grades.append(grade)#adding the received grade to the list
    weights.append(weight)#adding the received grade weight to the list
    average = sum([grades[i]*weights[i] for i in range(len(grades))])/sum(weights)#calculating the average of grades

    print("\nTwoja średnia wynosi: [", round(average,2),"]\n")#rounding the average to 2 decimal places
    print("|Ocena | Waga| ")

    for a,b in zip(grades,weights):
        print("[",a,"wagi",int(b),"]")
        #This code is effectively printing out each element of the "grades" list, 
        #along with its corresponding element in the "weight" list, with a format of [grade weight].
    next_grade = input("")
    try:
        if next_grade.lower() == "end" or grade.lower() == "end" or weight.lower() == "end":
            break
    except AttributeError:
        pass
    if next_grade.lower() == "delete":
        Delete_grade()
        #call definition for deleting grade and weight
