def print_hello(name: str = "неизвестный"):
    print(f"Привет, {name}!")


def main():
    print_hello()
    print_hello("Андрей")


if __name__ == "__main__":
    main()