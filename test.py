import json

global students
students = list()

def get_choice():
    print("\n**********Welcome To Student Database**************")
    print("Choice 1: add Student")
    print("Choice 2:search Student")
    print("Choice 4:add new student")
    print("Choice 3:print all")
    print("Choice 4:delete")
    print("Choice 5:quit")
    try:
        choice =int(input("Enter the choice :"))
    except :
        exit("\n invalid")
    return choice 

def add_student():
    student = {}
    student["regno"]   =  int(input("enter the reg number:"))
    student["name"]    =   input("enter the name:")
    student["mark"]    =   int(input("enter the mark :"))
    students.append(student)

    return


def search():
    global students
    regno = int(input("enter the rgeno want to search:"))
    s =students.get(regno,"not found")
    print(s)
    pass


def print_all():
    
    print("**************")
    for student in students :
        regno = student["regno"]
        name  = student["name"]
        mark  = student["mark"]

        print("enter the regno : ", regno)
        print("enter the name  : ", name)
        print("enter the mark  : ", mark)
        print("----------------------")
    print("**************")

def delete():
    print("Not implemented")

    pass


def pquit():

    with open ("student.json", "w") as f:
        temp = json.dump(students, f)


def load_data():
    global students
    with open ("student.json", "r") as f:
        try:
            students = json.load(f)
        except:
            print("Json data is invalid")
            pass


load_data()
while True:
    choice = get_choice()
    if choice == 1:
        add_student()
        
    elif choice == 2:
        search()

    elif choice == 3:
        print_all()

    elif choice == 4:
        delete()

    elif choice == 5:
        pquit()
        break

    else:
        print("wrong entry")    
                
                      
    
