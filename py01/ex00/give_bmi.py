from math import pow


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculates the BMI based on the height and weight"""
    return [w / pow(h, 2) for w, h in zip(weight, height)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Returns a list of booleans based on the BMI and the limit"""
    return [i > limit for i in bmi]


def main():
    return


if __name__ == "__main__":
    main()
