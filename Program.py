def Delete_grade():
    pass
grades = []
weights = []
next_grade = input("#========================================#\n\nJeżeli Chcesz zakończyć -> Wpisz [end]\nJeżeli Chcesz usunąć ocene -> Wpisz [delete] \nJeżeli Chcesz korzystać z programu -> Wciśnij [Enter]\n")
if next_grade.lower() == "end":
    exit()
while True:
    while True:
        grade = input("#========================================#\n\nPodaj ocenę : ")
        if next_grade.lower() == "end" or grade.lower() == "end": exit()
        elif grade == "": print("Nie podałeś oceny (Jeżeli chcesz zakończyć program wpisz \"end\"\n")
        else: break  
    while True:     
        weight = input("Podaj wagę oceny : ")
        try:
            if next_grade.lower() == "end" or grade.lower() == "end" or weight.lower() == "end":exit()
            elif weight == "": print("Nie podałeś wagi oceny (Jeżeli chcesz zakończyć program wpisz \"end\"\n\n#========================================#")
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


    

