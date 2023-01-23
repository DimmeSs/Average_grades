import os

# Windows romiar okna
os.system("mode con: cols=55 lines=20")
def design():
    a = "#" + "="*53 +"#"
    return a
grades = []
weights = []

def Delete_grade():
    print(design())
    print("\nLista ocen:",grades)
    while True:
        nr = input("\nPodaj miejsce oceny, którą chcesz usunąć \n(np. 1 lub 2 itp..) : ")
        if nr == "":
            print("Nie podałeś miejsca. Wpisz ponownie")
        elif len(grades) < int(nr):
            print("Nie ma w tym miejscu oceny")
        else:
            nr = int(nr)
            grades.pop(nr-1)
            weights.pop(nr-1)
            print("Aktualna lista ocen:",grades,"\n")
            break

print(design())
next_grade = input("\nJeżeli Chcesz zakończyć -> Wpisz [end]\nJeżeli Chcesz usunąć ocene -> Wpisz [delete]\nJeżeli Chcesz korzystać z programu -> Wciśnij [Enter]\n")
if next_grade.lower() == "end":
    exit()
elif next_grade.lower() == "delete":
    print("\nNie ma sensu teraz usuwać jak nie masz żadnych ocen :3\nPrzypuszczam że chcesz na początku dodać oceny :p")
while True:

    while True:
        print(design())
        grade = input("\nPodaj ocenę : ")
        if next_grade.lower() == "end" or grade.lower() == "end": exit()
        elif grade == "" or grade not in ["1", "1+", "2-", "2", "2+", "3-", "3", "3+", "4-", "4", "4+", "5-", "5", "5+", "6-", "6", "6+"]:
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


    

# def Delete_grade():
#     print(design())
#     grades =["3.0","4.5"]
#     weights =["3.0","4.5"]
#     print("\nLista ocen:",grades)
#     while True:
#         nr = input("\nPodaj miejsce oceny, którą chcesz usunąć \n(np. 1 lub 2 itp..) : ")
#         nr_d = 0
#         if nr == "":
#             print("Nie podałeś miejsca. Wpisz ponownie")
#         elif len(grades) < nr_d:
#             print("Nie ma w tym miejscu oceny")
#         else:
#             # nr = int(nr)
#             # nr-=1
#             grades.pop(nr_d)
#             weights.pop(nr_d)
#             print("Aktualna lista ocen:",grades,"\n")
#             break