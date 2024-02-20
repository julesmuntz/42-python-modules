from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """This is the King Class"""

    def __init__(
        self,
        first_name,
        family_name="Baratheon",
    ):
        """Constructor for the King Class"""
        super().__init__(first_name)
        self.family_name = family_name

    def set_eyes(self, eyes):
        """Method that sets the eyes of the King"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Method that sets the hairs of the King"""
        self.hairs = hairs

    def get_eyes(self):
        """Method that gets the eyes of the King"""
        return self.eyes

    def get_hairs(self):
        """Method that gets the hairs of the King"""
        return self.hairs
