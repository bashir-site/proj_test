from src.masks import calculate_taxes


if __name__ == "__main__":
    result = calculate_taxes(
        [100, 120, 68, 1300],
        10
    )
    print(result)