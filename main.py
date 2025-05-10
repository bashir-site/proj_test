from src.masks import calculate_taxes
from src.widget import number
from random import randint


if __name__ == "__main__":
    print(
        randint(1, 100)
    )

    # вызов переменной
    print(number)

    # вызов функции
    result = calculate_taxes(
        [100, 120, 68, 1300],
        number
    )
    print(result)