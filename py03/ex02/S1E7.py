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
        """Constructor for the Baratheon class."""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __repr__(self) -> str:
        """Representation of the Baratheon class."""
        return super().__repr__()

    def __str__(self) -> str:
        """String representation of the Baratheon class."""
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
        """Constructor for the Lannister class."""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __repr__(self) -> str:
        """Representation of the Lannister class."""
        return super().__repr__()

    def __str__(self) -> str:
        """String representation of the Lannister class."""
        return super().__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Method that creates a Lannister."""
        return Lannister(first_name, is_alive)
