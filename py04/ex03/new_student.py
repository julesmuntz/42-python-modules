import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15-character string."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """This is a Student class."""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        try:
            self.login = self.name[0] + self.surname
        except Exception:
            self.login = ""
