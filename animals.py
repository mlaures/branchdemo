import sys
if sys.version_info < (3,):
    input = raw_input

def sounds(animal):
    if animal == "cat":
        print("meow")
    elif animal == "dog":
        print("woof")
    elif animal == "duck":
        print("quack")
    else:
        print("are you sure that's an animal?")

def main():
    animal = input("which animal?: ")
    sounds(animal)

if __name__=="__main__":
    main()
