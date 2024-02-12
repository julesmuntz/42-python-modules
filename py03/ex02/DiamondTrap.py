from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """This is the King Class"""

    def __init__(
        self,
        first_name,
        family_name="Baratheon",
    ):
        super().__init__(first_name)
        self.family_name = family_name

    def set_eyes(self, eyes):
        self.eyes = eyes

    def set_hairs(self, hairs):
        self.hairs = hairs

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs
