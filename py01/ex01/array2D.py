def slice_me(family: list, start: int, end: int) -> list:
    if type(family) != list:
        return print("Error: not a list")
    start = abs(start)
    end = abs(end)
    size = len(family[0])
    for i in family:
        if len(i) != size:
            return print("Error: lists are not the same size")
        size = len(i)
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    print(f"The new shape is : ({start}, {end})")
    return family[start:end]