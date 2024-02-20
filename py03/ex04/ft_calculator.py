class calculator:
    """This is a calculator class"""

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot product method"""
        dot_product = sum(V1[i] * V2[i] for i in range(len(V1)))
        print(f"Dot product is: {dot_product}")

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Addition method"""
        add_vector = [V1[i] + V2[i] for i in range(len(V1))]
        print(f"Add Vector is: {add_vector}")

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Substraction method"""
        sous_vector = [V1[i] - V2[i] for i in range(len(V1))]
        print(f"Sous Vector is: {sous_vector}")
