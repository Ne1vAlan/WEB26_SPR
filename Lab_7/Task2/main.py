from models import Animal, Dog, Cat

def main():
    animals = [
        Dog(name="Rex",   age=3, weight=28.5, breed="German Shepherd"),
        Dog(name="Buddy", age=5, weight=22.0, breed="Labrador"),
        Cat(name="Luna",  age=2, weight=4.2,  indoor=True),
        Cat(name="Mochi", age=4, weight=3.8,  indoor=False),
    ]

    print("=== All Animals ===")
    for animal in animals:
        print(animal)

    print("\n=== Polymorphism: speak() ===")
    for animal in animals:
        print(animal.speak())

    print("\n=== Descriptions ===")
    for animal in animals:
        print(animal.describe())

    print("\n=== Unique Methods ===")
    for animal in animals:
        if isinstance(animal, Dog):
            print(animal.fetch())
        elif isinstance(animal, Cat):
            print(animal.purr())


if __name__ == "__main__":
    main()