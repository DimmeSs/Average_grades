import os
from termcolor import colored
#Text Language -> English

#Window size
os.system("mode con: cols=55 lines=20")

def design():  #definition that returns characters for cmd design
    a = "#" + "="*51 +"#"
    return a
   
grades = [] #a list where the grades entered by the user are kept
weights = [] #a list where the weights entered by the user are kept

def Delete_grade(): #definition that allows you to select a grades and remove it along with its weight
    print(design())
    print("\nGrades list:",grades)
    while True:
        nr = input("\nEnter the location of the grade you want to remove \n(Example: 1 or 2 etc..) : ")
        if nr == "":
            print(colored("[Error] You didn't specify a place.Please retype ","red")) #colored makes text color => red
        elif len(grades) < int(nr):
            print(colored("[Error] There is no grade here","red"))
        else:
            nr = int(nr)
            print("The chosen Grade : [",grades[nr-1],"with weight",weights[nr-1],"]")
            grades.pop(nr-1)#remove selected grade 
            weights.pop(nr-1)#remove selected weight
            for a,b in zip(grades,weights):
                print(colored("\nGrades list:\n|Grades|Weight| ","light_blue"))
                print(colored("|"+str(a)+" ======= "+str(int(b))+"|","light_blue"))
            try :
                average = sum([grades[i]*weights[i] for i in range(len(grades))])/sum(weights) #calculating the average of grades
                print("\nYour average is: [", round(average,2),"]\n") #rounding the average to 2 decimal places
            except ZeroDivisionError:
                print(colored("You have removed the grade, so you can't calculate the average\n","red"))
            break #go back to program

print(design())
next_grade = input("\nIf You want to exit -> Type [end]\nIf You want to delete grades -> Type [delete]\nIf You want to use the program -> Press [Enter]\n")#info
if next_grade.lower() == "end":
    exit()
elif next_grade.lower() == "delete":
    print(colored("\n[Error] No point in deleting now without any ratings :3\nI suppose you want to add grades first :p","red"))#"that'w what she said"
while True:

    while True:
        print(design())
        grade = input("\nGive grade: ") #retrieving a grade from the user
        if next_grade.lower() == "end" or grade.lower() == "end": exit()
        elif grade == "" or grade not in ["1", "1+", "2-", "2", "2+", "3-", "3", "3+", "4-", "4", "4+", "5-", "5", "5+", "6-", "6", "6+"]:#Grade can't be < 0.75 and have to be < 7 
            print(colored("[Error] Invalid grade \n(If you want to end the program type [end] )\n","red"))
        else: break  

    while True:     
        weight = input("Enter grade weight : ") #retrieving  grade weight from the user
        try:
            if next_grade.lower() == "end" or grade.lower() == "end" or weight.lower() == "end":exit()
            elif weight == "": 
                print(colored("[Error] You did not provide the grade weight \n(If you want to exit -> Type [end]\n","red"))
                print(design())
            elif weight == "delete":
                print(colored("\n[Error] No point in deleting now without any ratings :3\nI suppose you want to add grades first :p","red"))
            else:break
        except AttributeError:
            break

    weight = float(weight)
    if '+' in grade: #converting a [grade+] to float and calculating(for example 4+ to float 4+0.50)
        grade = float(grade.replace('+','')) + 0.5
    elif '-' in grade: #converting a [grade-] to float and calculating(for example 4- to float 4-0.25)
        grade = float(grade.replace('-','')) - 0.25
    else:
        grade = float(grade)
        
    grades.append(grade) #adding the received grade to the list
    weights.append(weight) #adding the received grade weight to the list
    average = sum([grades[i]*weights[i] for i in range(len(grades))])/sum(weights)#calculating the average of grades

    print("\nYour average is: [", round(average,2),"]\n")#rounding the average to 2 decimal places
    print(colored("|Grades|Weight| ","light_blue"))

    for a,b in zip(grades,weights):
        print(colored("|"+str(a)+" ======= "+str(int(b))+"|","light_blue"))
        #This code is effectively printing out each element of the "grades" list, 
        #along with its corresponding element in the "weight" list, with a format of |grade ======= weight|.
    next_grade = input("\nPress [Enter] to add new Grade\n")
    try:
        if next_grade.lower() == "end" or grade.lower() == "end" or weight.lower() == "end":
            break
    except AttributeError:
        pass
    if next_grade.lower() == "delete":
        Delete_grade() #call definition for deleting grade and weight
        
