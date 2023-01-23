import os

# Windows romiar okna
#os.system("mode con: cols=55 lines=20")
def design():
    a = "#" + "="*53 +"#"
    return a
#=====================================================#
grades = []
weights = []

def Delete_grade():
    print("\n#========================================#\nLista ocen:",grades)
    while True:
        nr = input("\nPodaj miejsce oceny, którą chcesz usunąć (np. 1 lub 2 itp..) : ")
        if nr == "":
            print("Nie podałeś miejsca. Wpisz ponownie")
        else:
            nr = int(nr)
            nr-=1
            grades.pop(nr)
            weights.pop(nr)
            print("Aktualna lista ocen:",grades,"\n")
            break

print(design())
next_grade = input("\nJeżeli Chcesz zakończyć -> Wpisz [end]\nJeżeli Chcesz usunąć ocene -> Wpisz [delete] \nJeżeli Chcesz korzystać z programu -> Wciśnij [Enter]\n")
if next_grade.lower() == "end":
    exit()
elif next_grade.lower() == "delete":
    print("\nNie ma sensu teraz usuwać jak nie masz żadnych ocen :3\nPrzypuszczam że chcesz na początku dodać oceny :p")
while True:
    while True:
        print(design())
        grade = input("\nPodaj ocenę : ")
        if next_grade.lower() == "end" or grade.lower() == "end": exit()
        #Mess below but i have no idea what else do i have to do
        elif grade == "" or grade != "1" or grade != "1+"or grade != "2-"or grade != "2"or grade != "2+"or grade != "3-"or grade != "3"or grade != "3+"or grade != "4-"or grade != "4"or grade != "4+"or grade != "5-"or grade != "5"or grade != "5+"or grade != "6-"or grade != "6"or grade != "6+":
            print("Niepoprawna ocena (Jeżeli chcesz zakończyć program wpisz [end] )\n")
        else: break  
    while True:     
        weight = input("Podaj wagę oceny : ")
        try:
            if next_grade.lower() == "end" or grade.lower() == "end" or weight.lower() == "end":exit()
            elif weight == "": 
                print("Nie podałeś wagi oceny (Jeżeli chcesz zakończyć program wpisz \"end\"\n")
                print(design())
            else:break
        except AttributeError:
            break
    weight = float(weight)
    if '+' in grade:
        grade = float(grade.replace('+','')) + 0.5
    elif '-' in grade:
        grade = float(grade.replace('-','')) - 0.25
    else:
        grade = float(grade)
        
    grades.append(grade)
    weights.append(weight)
    average = sum([grades[i]*weights[i] for i in range(len(grades))])/sum(weights)

    print("\nTwoja średnia wynosi: [", round(average,2),"]\n")
    print("|Ocena | Waga| ")

    for a,b in zip(grades,weights):
        print("[",a,"wagi",int(b),"]")
    next_grade = input("")
    try:
        if next_grade.lower() == "end" or grade.lower() == "end" or weight.lower() == "end":
            break
    except AttributeError:
        pass
    if next_grade.lower() == "delete":
        Delete_grade()


    

