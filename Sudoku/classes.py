class RangeError(Exception):
    def __str__(self):
        return "올바른 범위의 수를 입력해 주세요"


class NonNumberError(Exception):
    def __str__(self):
        return "숫자를 입력해 주세요"

