from setuptools import setup


def main():
    with open("README.md", "r") as f:
        f.read()

    setup(
        name="ft_package",
        version="0.0.1",
        description="A sample test package",
        url="http://example.com",
        author="Jules Muntz Berger",
        author_email="julmuntz@student.42.fr",
        license="MIT",
    )
    return


if __name__ == "__main__":
    main()
