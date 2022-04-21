import random as rd
from pprint import pprint


def select_idx(area_num: int) -> list:
    """
    :param area_num: area number to select detail index
    :return: couple of index
    """
    candid_list = list(range(area_num*3, area_num*3 + 3))
    idx_in_area_1 = rd.choice(candid_list)
    candid_list.remove(idx_in_area_1)

    idx_in_area_2 = rd.choice(candid_list)

    return [idx_in_area_1, idx_in_area_2]


def place_num_into_map(map_base: list, num_shuffle: int) -> list:
    """
    :param map_base: map to shuffle
    :param num_shuffle: number for how much to shuffle
    :return: shuffled map
    """
    count = 0
    while True:
        if count == num_shuffle:
            return map_base
        area_num_row = rd.randint(0, 2)
        idx_in_area_row_1, idx_in_area_row_2 = select_idx(area_num_row)

        area_num_column = rd.randint(0, 2)
        idx_in_area_column_1, idx_in_area_column_2 = select_idx(area_num_column)

        for row in range(9):
            for column in range(9):
                map_base[row][idx_in_area_column_1], map_base[row][idx_in_area_column_2] = \
                    map_base[row][idx_in_area_column_2], map_base[row][idx_in_area_column_1]

        for column in range(9):
            for row in range(9):
                map_base[idx_in_area_row_1][column], map_base[idx_in_area_row_2][column] = \
                    map_base[idx_in_area_row_2][column], map_base[idx_in_area_row_1][column]

        count += 1


def make_solution_map(difficulty: int) -> list:
    """
    :param difficulty: select the difficulty among the 1 to 10
    :return: create a background map according to the number of lines and difficulty
    """
    map_base = []
    for idx_in_area in range(3):
        for num_area in range(3):
            map_base.append(list(range(1, 10))[num_area*3 + idx_in_area:] + list(range(1, 10))[:num_area*3 + idx_in_area])

    return place_num_into_map(map_base, rd.randint(1, 10))


pprint(make_solution_map(1))
