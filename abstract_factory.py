# -*- coding: utf-8 -*-

import random
from typing import Type


class Pet:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class Dog(Pet):
    def speak(self) -> None:
        print("woof")

    def __str__(self) -> str:
        return f"Dog<{self.name}>"


class Cat(Pet):
    def speak(self) -> None:
        print("meow")

    def __str__(self) -> str:
        return f"Cat<{self.name}>"


class PetShop:
    """A pet shop"""

    def __init__(self, animal_factory: Type[Pet]) -> None:
        """pet_factory is our abstract factory.  We can set it at will."""

        self.pet_factory = animal_factory

    def buy_pet(self, name: str) -> Pet:
        """Creates and shows a pet using the abstract factory"""

        pet = self.pet_factory(name)
        print(f"Here is your lovely {pet}")
        return pet


# Show pets with various factories
def main() -> None:
    """
    # A Shop that sells only cats
    >>> cat_shop = PetShop(Cat)
    >>> pet = cat_shop.buy_pet("Lucy")
    Here is your lovely Cat<Lucy>
    >>> pet.speak()
    meow
    """


if __name__ == "__main__":
    shop = PetShop(Dog)
    import doctest

    doctest.testmod()
