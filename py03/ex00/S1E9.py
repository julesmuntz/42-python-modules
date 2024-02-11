from abc import ABC, abstractmethod


class Character(ABC):
    """Docstring for Parent Class"""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Docstring for Parent Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Docstring for Parent Method"""
        self.is_alive = False


class Stark(Character):
    """Docstring for Child Class"""

    def __init__(self, first_name, is_alive=True):
        """Docstring for Child Constructor"""
        super().__init__(first_name, is_alive)
