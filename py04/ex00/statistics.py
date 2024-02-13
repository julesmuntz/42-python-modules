def ft_statistics(*args: any, **kwargs: any) -> None:
    for key, value in kwargs.items():
        try:
            mean = sum(args) / len(args)
            median = sorted(args)[len(args) // 2]
            quartile = [sorted(args)[len(args) // 4],
                        sorted(args)[3 * len(args) // 4]]
            variance = sum((x - mean) ** 2 for x in args) / len(args)
            std = variance**0.5
            if value == "mean" and key:
                print(f"mean : {mean}")
            elif value == "median" and key:
                print(f"median : {median}")
            elif value == "quartile" and key:
                print(f"quartile : {quartile}")
            elif value == "std" and key:
                print(f"std : {std}")
            elif value == "var" and key:
                print(f"var : {variance}")
        except Exception:
            print("ERROR")
