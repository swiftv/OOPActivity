#Animal rescue centre program

#class definitions
#animal class 
class animal:
    name = ""
    classification = ""
    arrival_date = ""
    # Setters and getters
    def set_name(self, data):
        self.name = data
    def set_type(self, data):
        self.classification = data
    def set_arrival_date(self, data):
        self.arrival_date = data
    def get_attributes(self):
        return [self.name, self.classification, self.arrival_date]

class dog(animal):
    is_trained = False
    favourite_toy = ""
    def set_is_trained(self, data):
        self.is_trained = data
    def set_favourite_toy(self, data):
        self.favourite_toy = data
    def get_attributes(self):
        return [self.name, self.classification, self.arrival_date, self.is_trained, self.favourite_toy]

class cat(animal):
    indoor_only = False

    def set_indoor_only(self, data):
        self.indoor_only = data
    def get_attributes(self):
        return [self.name, self.classification, self.arrival_date, self.indoor_only]
#subprograms


#menu

def menu():
    option = ""
    while option != "3":
        print("1. New Animal")
        print("2. Output animals")
        print("3. Quit")
        option = input(":")
        match option:
            case "1":
                new_animal()
            case "2":
                output_animals()

#add a a new animal to add to the rescue
def new_animal():
    animal_type = input("Enter the type of animnal: ")
    match animal_type.lower():
        case "dog":
            new_dog()
        case "cat":
            new_cat()
    
def new_dog():
    animal_object = dog()
    animal_name = input("Enter the name of the animal: ")
    arrived = input("Enter the date of the arrival")
    is_trained = input("Is the dog trained? (yes/no): ").lower() == "yes"
    favourite_toy = input("Enter the dog's favourite toy: ")
    animal_object.set_name(animal_name)
    animal_object.set_type("dog")
    animal_object.set_arrival_date(arrived)
    animal_object.set_is_trained(is_trained)
    animal_object.set_favourite_toy(favourite_toy)
    rescue.append(animal_object)  

def new_cat():
    animal_object = cat()
    animal_name = input("Enter the name of the animal: ")
    arrived = input("Enter the date of the arrival")
    indoor_only = input("Is the cat indoor only? (yes/no): ").lower() == "yes"
    animal_object.set_name(animal_name)
    animal_object.set_type("cat")
    animal_object.set_arrival_date(arrived)
    animal_object.set_indoor_only(indoor_only)
    rescue.append(animal_object)

#output the animals in the rescue
def output_animals():
    for animal in rescue:
        print(animal.get_attributes())

#main program
rescue = []
menu()