from itertools import permutations


def possible_permutations(a_list):
    return (list(p) for p in permutations(a_list))
    # return [list(p) for p in permutations(a_list)]


def get_permutations(a_list, idx=0):
    if idx == len(a_list) - 1:
        print("".join(a_list))
    for j in range(idx, len(a_list)):
        words_list = [c for c in a_list]
        words_list[idx], words_list[j] = words_list[j], words_list[idx]

        get_permutations(words_list, idx + 1)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in get_permutations([1, 2, 3])]
