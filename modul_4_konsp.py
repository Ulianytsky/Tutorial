# def amount_payment(payment):
#     sum = 0
#     for i in payment:
#         if i > 0:
#             sum = sum + i

#     return (sum)


# def prepare_data(data):
#     lst = [1, -3, 4, 100, 0, -5, 10, 1, 1]
#     lst.sort()
#     lst.pop(0)
#     lst.pop()
#     print(lst)


# def prepare_data(data):
#     lst = sorted(data)
#     lst1 = lst.pop(0)
#     lst2 = lst.pop()
#     print(lst)
#     return lst
# def get_grade(key):
#     grades = {
#         "F": 1,
#         "FX": 2,
#         "E": 3,
#         "D": 3,
#         "C": 4,
#         "B": 5,
#         "A": 5
#     }
#     return grades.get(key, None)


# def get_description(key):
#     descriptions = {
#         "F": "Unsatisfactorily",
#         "FX": "Unsatisfactorily",
#         "E": "Enough",
#         "D": "Satisfactorily",
#         "C": "Good",
#         "B": "Very good",
#         "A": "Perfectly"
#     }
#     return descriptions.get(key, None)


# if __name__ == "__main__":
#     print(get_description("F"))


def split_list(scores):
    if not scores:  # если список пуст, возвращаем два пустых списка
        return [], []

    mean = sum(scores) / len(scores)  # находим среднее значение балла

    lower = []  # список для значений меньше или равных среднему
    higher = []  # список для значений строго больше среднего

    for score in scores:
        if score <= mean:
            lower.append(score)
        else:
            higher.append(score)

    return lower, higher
