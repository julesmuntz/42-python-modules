from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(
        self,
        first_name,
        is_alive=True,
        family_name="Baratheon",
        eyes="brown",
        hairs="dark",
    ):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __repr__(self) -> str:
        return super().__repr__()

    def __str__(self) -> str:
        return super().__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(
        self,
        first_name,
        is_alive=True,
        family_name="Lannister",
        eyes="blue",
        hairs="light",
    ):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __repr__(self) -> str:
        return super().__repr__()

    def __str__(self) -> str:
        return super().__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        return Lannister(first_name, is_alive)
