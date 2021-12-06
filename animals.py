import sys
if sys.version_info < (3,):
    input = raw_input

def sounds(animal):
    if animal == "cat":
        print("meow")
    elif animal == "dog":
        print("woof")
    else:
        print("are you sure that's an animal?")
    // this is from my even cat
    000000asdfghjklkjhgfdsa000000

def main():
    animal = input("which animal?: ")
    sounds(animal)

if __name__=="__main__":
    main()
