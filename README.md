# classes_and_objects
1.Zoo

Create a class Zoo. It should have a class attribute called __animals that stores the total count of the animals in
the zoo. The __init__ method should only receive the name of the zoo. There you should also create 3 empty lists
(mammals, fishes, birds). The class should also have 2 more methods:

-> add_animal(species, name) - based on the species adds the name to the corresponding list
-> get_info(species) - based on the species returns a string in the following format:
"{Species} in {zoo_name}: {names}
Total animals: {total_animals}"

On the first line you will receive the name of the zoo. On the second line you will receive number n. On the next n
lines, you will receive animal info in the format: "{species} {name}". Add the animal to the zoo to the
corresponding list. The "species" command will be mammal, fish, or bird.

On the final line you will receive a species. At the end, print the info for that species and the total count of animals
in the zoo.

2.Vehicle

Create a class Vehicle. The __init__ method should receive a type (str), a model (str), and a price (int). You
should also set an owner to None. The class should have the following methods:

-> buy(money, owner)
    If the person has enough money and the vehicle has no owner, sets the owner to the given one and
    returns: "Successfully bought a {type}. Change: {change}". Change should be
    formatted to the second decimal place.

    If the money is not enough, return: "Sorry, not enough money"
    If the car already has an owner, return: "Car already sold"
-> sell() - if the car has an owner, set it to None again. Otherwise, return: "Vehicle has no owner"
-> __repr__() - returns "{model} {type} is owned by: {owner}" if the vehicle has an owner.

Otherwise, return: "{model} {type} is on sale: {price}"

3.Email

Create class Email. The __init__ method should receive sender, receiver and a content. It should also have
a default set to False attribute called is_sent. The class should have two additional methods:

-> send() - sets the is_sent attribute to True
-> get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"

You will receive some information (separated by single space) until you receive the command "Stop". The first
element will be the sender, the second one – the receiver and the third one – the content. On the final line you will
be given the indices of the sent emails separated by comma and space ", ".

Call the send() method for the given indices of emails. For each email call the get_info() method.