class Animal:
    def __init__(self, name: str, age: int, weight: float):
        self.name = name
        self.age = age
        self.weight = weight

    def speak(self) -> str:
        return "..."

    def describe(self) -> str:
        return f"{self.name} is {self.age} years old and weighs {self.weight} kg"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name}, age={self.age}, weight={self.weight})"


class Dog(Animal):
    def __init__(self, name: str, age: int, weight: float, breed: str):
        super().__init__(name, age, weight)
        self.breed = breed

    def speak(self) -> str:
        return f"{self.name} says: Woof!"

    def fetch(self) -> str:
        return f"{self.name} fetches the ball!"

    def __str__(self) -> str:
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"


class Cat(Animal):
    def __init__(self, name: str, age: int, weight: float, indoor: bool):
        super().__init__(name, age, weight)
        self.indoor = indoor

    def speak(self) -> str:
        return f"{self.name} says: Meow!"

    def purr(self) -> str:
        return f"{self.name} is purring..."

    def __str__(self) -> str:
        lifestyle = "indoor" if self.indoor else "outdoor"
        return f"Cat(name={self.name}, age={self.age}, lifestyle={lifestyle})"