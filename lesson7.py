class Animal:

    num_of_inst = 0

    def __init__(self,animal_name, animal_voice):
        self.animal_name = animal_name
        self.animam_voice = animal_voice
        Animal.num_of_inst += 1

    def voice(self):
        print(self.animam_voice.upper())

    def say_who(self):
        print(f'I`m {self.__class__.__name__} and my name is {self.animal_name}')

def num_inst():
    print(Animal.num_of_inst)

class Lion(Animal):
    def __init__(self, animal_name):
        super().__init__(animal_name, "arrrrr")

    def say_who(self):
        print("I`m LION")


class Horse(Animal):
    pass

class Bear(Animal):

    def __init__(self,animal_name, animal_voice):
        super().__init__(animal_name ,animal_voice=animal_voice)

    def voice(self):
        print(self.animam_voice.lower() + self.animal_name.upper() + self.animam_voice.lower())

    def say_who(self):
        print(self.animal_name[::-1])

lion = Lion("Simba")
horse = Horse("Pegas", "igogo")
bear = Bear('Baloo', "RRR")

num_inst()