#Animal rescue centre program

#class definitions


#subprograms


#menu

def menu():
    option = ""
    while option != "3":
        print("1. New Animal")
        print("2.  Output animals")
        print("3. Quit")
        option = input(":") 
        match option:
        case "1" : new_animal()
        case "2" : output_animals()

#add a a new animal to add to the rescue
def new_animal():
    animal_type = input("Enter the type of animnal: ")
    animal_name = input("Enter the name of the animal: ")
    arrived = input("Enter the date of the arrival")

#output the animals in the rescue
def output_animals():
    print()

#main program

menu()