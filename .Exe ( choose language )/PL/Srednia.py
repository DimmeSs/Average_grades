import os
from termcolor import colored
#Język tekstu -> angielski

#Rozmiar okna
os.system("mode con: cols=55 lines=20")

def design():  #definicja, która zwraca znaki dla wyglądu w cmd
    a = "#" + "="*51 +"#"
    return a
   
grades = [] #lista, na której przechowywane są oceny wprowadzone przez użytkownika
weights = [] #lista, na której przechowywane są wagi wprowadzone przez użytkownika

def Delete_grade(): #definicja, która pozwala wybrać ocene i usunąć je wraz z wagą
    print(design())
    print("\nLista ocen:",grades)
    while True:
        nr = input("\nWprowadź lokalizację oceny, którą chcesz usunąć \n(Przykład: 1 lub 2 itd.) : ")
        if nr == "":
            print(colored("[Error] Nie określono miejsca. Wpisz ponownie ","red")) #colored powoduje, że kolor tekstu => czerwony
        elif len(grades) < int(nr):
            print(colored("[Error] Nie ma takiej oceny","red"))
        else:
            nr = int(nr)
            print("Wybrana ocena: [",grades[nr-1],"wagi",weights[nr-1],"]")
            grades.pop(nr-1) #usuń wybraną ocenę 
            weights.pop(nr-1) #usuń wybraną wagę
            for a,b in zip(grades,weights):
                print(colored("\nLista ocen:\n|Ocena | Waga | ","light_blue"))
                print(colored("|"+str(a)+" ======= "+str(int(b))+"|","light_blue"))
            try :
                average = sum([grades[i]*weights[i] for i in range(len(grades))])/sum(weights) #calculating the average of grades
                print("\nTwoja średnia wynosi: [", round(average,2),"]\n") #rounding the average to 2 decimal places
            except ZeroDivisionError:
                print(colored("Usunięto ocenę, więc nie można obliczyć średniej\n","red"))
            break #go back to program

print(design())
next_grade = input("\nJeśli chcesz wyjść -> Wpisz [end]\nJeśli chcesz usunąć oceny -> Wpisz [delete]\nJeśli chcesz skorzystać z programu -> Naciśnij [Enter]\n")#info
if next_grade.lower() == "end":
    exit()
elif next_grade.lower() == "delete":
    print(colored("\n[Error] Nie ma sensu usuwać teraz bez żadnych ocen :3\nChyba najpierw chcesz dodać ocene :p","red"))#"that'w what she said"
while True:

    while True:
        print(design())
        grade = input("\nPodaj ocenę: ") #pobieranie oceny od użytkownika
        if next_grade.lower() == "end" or grade.lower() == "end": exit()
        elif grade == "" or grade not in ["1", "1+", "2-", "2", "2+", "3-", "3", "3+", "4-", "4", "4+", "5-", "5", "5+", "6-", "6", "6+"]:
            #Ocena nie może być mniejsza od 0.75 i musi być większa/równa 1 ale mniejsza niż 8 
            print(colored("[Error] Nieprawidłowa ocena \n(Jeśli chcesz zakończyć program, wpisz [end] )\n","red"))
        else: break  

    while True:     
        weight = input("Wprowadź wagę oceny : ") #pobieranie wagi oceny od użytkownika
        try:
            if next_grade.lower() == "end" or grade.lower() == "end" or weight.lower() == "end":exit()
            elif weight == "": 
                print(colored("[Error] Nie podałeś wagi oceny \n(Jeśli chcesz wyjść -> Wpisz [end]\n","red"))
                print(design())
            elif weight == "delete":
                print(colored("\n[Error] Nie ma sensu usuwać teraz bez żadnych ocen :3\nChyba najpierw chcesz dodać ocene :p","red"))
            else:break
        except AttributeError:
            break

    weight = float(weight)
    if '+' in grade: #konwertowanie [oceny+] na zmiennoprzecinkowe i obliczanie (na przykład 4+ na zmiennoprzecinkowe 4+0,50)
        grade = float(grade.replace('+','')) + 0.5
    elif '-' in grade: #konwertowanie [stopień-] na zmiennoprzecinkowe i obliczanie (na przykład 4- na zmiennoprzecinkowe 4-0,25)
        grade = float(grade.replace('-','')) - 0.25
    else:
        grade = float(grade)
        
    grades.append(grade) #dodanie otrzymanej oceny do listy
    weights.append(weight) #dodanie otrzymanej wagi ocen do listy
    average = sum([grades[i]*weights[i] for i in range(len(grades))])/sum(weights)#obliczanie średniej ocen

    print("\nTwoja średnia wynosi: [", round(average,2),"]\n")#zaokrąglenie średniej do 2 miejsc po przecinku i wyświetlenie jej
    print(colored("|Ocena | Waga | ","light_blue"))

    for a,b in zip(grades,weights):
        print(colored("|"+str(a)+" ======= "+str(int(b))+"|","light_blue"))
        # Ten kod skutecznie drukuje każdy element listy „ocen”,
        #wraz z odpowiadającym mu elementem na liście „waga”, w formacie |grade ======= waga|.
    next_grade = input("\nNaciśnij [Enter], aby dodać nową ocenę\n")
    try:
        if next_grade.lower() == "end" or grade.lower() == "end" or weight.lower() == "end":
            break
    except AttributeError:
        pass
    if next_grade.lower() == "delete":
        Delete_grade() #definicja wywołania do usuwania oceny i wagi
        
