from abc import ABC, abstractmethod


class Character(ABC):
    """Docstring for Parent Class"""

    @abstractmethod
    def __init__(self, first_name, is_alive=True,
                 family_name=None, eyes=None, hairs=None):
        """Docstring for Parent Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Docstring for Parent Method"""
        self.is_alive = False

    def __repr__(self) -> repr:
        """Docstring for __repr__"""
        return self.__str__()

    def __str__(self) -> str:
        """Docstring for __str__"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs})'"


class Stark(Character):
    """Docstring for Child Class"""

    def __init__(self, first_name, is_alive=True):
        """Docstring for Child Constructor"""
        super().__init__(first_name, is_alive)
