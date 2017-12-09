'''Codefights Interview practice - Hash Tables - "groupingDishes"'''
def groupingDishes(dishes):
    '''groupingDishes(list[list1, list2, ...]) -> _list[_list1, _list2, ...]
    Given a list of dishes (list of ingredients) return a new list of lists
    structured as ingredient and dishes where it is present as follow:
    \t  [
    \t      [i1, d1, d2, d4, d6],
    \t      [i2, d3, d4, d6],
    \t      ...
    \t  ]'''
    _hash = {}
    for line in dishes:
        for i in line[1:]:
            try:
                _hash[i] = sorted(_hash[i] + [line[0]])
            except KeyError:
                _hash[i] = [line[0]]

    return [[r] + _hash[r] for r in sorted(_hash.keys()) if len(_hash[r]) > 1]

DISHES = [["Pasta", "Tomato Sauce", "Onions", "Garlic"],
          ["Chicken Curry", "Chicken", "Curry Sauce"],
          ["Fried Rice", "Rice", "Onions", "Nuts"],
          ["Salad", "Spinach", "Nuts"],
          ["Sandwich", "Cheese", "Bread"],
          ["Quesadilla", "Chicken", "Cheese"]]

EXPECTED_OUTPUT = [["Cheese", "Quesadilla", "Sandwich"],
                   ["Chicken", "Chicken Curry", "Quesadilla"],
                   ["Nuts", "Fried Rice", "Salad"],
                   ["Onions", "Fried Rice", "Pasta"]]

OUTPUT = groupingDishes(DISHES)
print(OUTPUT, OUTPUT == EXPECTED_OUTPUT)
help(groupingDishes)
