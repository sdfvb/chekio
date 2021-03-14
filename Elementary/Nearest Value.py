from dataclasses import dataclass


@dataclass
class Num:
    value: int = None
    vector: int = None


def nearest_value(values: set, one: int) -> int:
    near_num = Num()
    for num in values:
        if not near_num.value or abs(num - one) < near_num.vector or (
                abs(num - one) == near_num.vector and num < near_num.value):
            near_num.vector = abs(num - one)
            near_num.value = num

    return near_num.value


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
