# Name: Jay Williams
# Program Purpose: This program demonstrates how to use a list, including:
#   finding number of items in the list, sorting the list, adding/removing items,    
#   copying a list of items into another list, and changing the data in the list.

dogs = ["Sadie", "Molly", "Ella", "Milo", "Buddy", "Rocky", "AnnaBelle", "Gonzo", "Sweetie-Pie", "Diego", "Jack", "Jasmine",
        "Olive"]
dogs2 = []

def main():
        how_many = len(dogs)
        print("\nNumber of dogs in the list: " + str(how_many))
        print("\nOriginal list of dog names: ")
        print(dogs)

        dogs.reverse()
        print("\nList from last to first:")
        print(dogs)

        dogs.sort()
        print("\nAlphabetized list:")
        print(dogs)

        dogs.sort(reverse = True)
        print("nList in reverse alphabetized order:")
        print(dogs)

        dogs.append("Ranger")
        print("\nAdd a dog to the end of a list:")
        print(dogs)

        doggy = dogs.pop(0)
        print("\nPop a fog off (remove) from the fron of the list:")
        print(dogs)
        print(doggy + "was removed from the front of the list.")

        another_dog = dogs.pop (3)
        print("\nNote: position number in a list begin with 0, not with 1")
        print("Pop a dog off from position 3 (which is the 4th dog) in the list:")
        print(dogs)
        print(another_dog + "was removed from postion 3 of the list.")

        dogs.remov ('AnnaBelle')
        print("\nRemove a dog by name rather than position in the list:")
        print(dogs)

        dogs2 = dogs
        print("nA list can be copied into another list by setting on equal to the other:")
        print(dogs)
        print(dogs2)

        print("nUse a FOR loop to give each dog the same last name:")
        for i in range(len(dogs)):
                dogs[i] = dogs[i] + "Williams"
        print(dogs)
        
main()
