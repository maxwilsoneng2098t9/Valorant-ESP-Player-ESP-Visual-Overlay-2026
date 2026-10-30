"""Entry point for engine."""

from utils import optimize


def main():
    result = optimize(100)
    print(f"Project: {result}")


if __name__ == "__main__":
    main()
