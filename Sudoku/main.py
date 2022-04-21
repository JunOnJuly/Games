import functions
from classes import *

if __name__ == '__main__':
    solution = functions.make_solution_map()
    while True:
        try:
            difficulty = input('난이도를 선택하세요 (1~4) : ')
            if difficulty.isdigit():
                if 0 < int(difficulty) < 5:
                    difficulty = int(difficulty)
                    break
                else:
                    raise RangeError
            else:
                raise NonNumberError

        except RangeError:
            print(RangeError)
            continue

        except NonNumberError:
            print(NonNumberError)
            continue

        else:
            break

    problem = functions.make_problem_map(solution, difficulty)

