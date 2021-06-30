class Zoo:
    __animals = 0
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []
    
    def get_animals_count(self):
        return self.__animals

    def add_animals(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        
        self.__animals += 1

    def get_info(self,species):
        if species == "mammal":
            return f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}"
        if species == "fish":
            return f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}"
        if species == "bird":
            return f"Birds in {self.zoo_name}: {', '.join(self.birds)}"

zoo_name = input()
n = int(input())
zoo = Zoo(zoo_name)
for _ in range(n):
    species, name = input().split()
    zoo.add_animals(species, name)

searched_species = input()
print(zoo.get_info(searched_species))
print(f"Total animals: {zoo.get_animals_count()}")