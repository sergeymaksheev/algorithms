
def binary_search(lst: list[int], value):
    lst.sort()
    while len(lst) > 1:
        middle = int(len(lst)/2)
        lst = lst[:middle] if value < lst[middle] else lst[middle:]
    if len(lst) == 1:
        return value == lst[0]
    
    return False
 
binary_search([2,3,4,5,6,7,8,9], 1)

# Recurtion

def binary_search_rec(lst: list[int], value: int)-> bool:
    len_lst = len(lst)
    if not len_lst:
        return False

    middle = int(len_lst/2)
    if len_lst == 1:
        return value == lst[0]

    lst = lst[:middle] if value < lst[middle] else lst[middle:] 
    return binary_search(lst=lst, value=value)


assert binary_search([2,3,4,5,6,7,8,9], 2)
assert binary_search([2,3,4,5,7,8,9], 9)
assert binary_search([2,3,4,5,6,7,8,9], 5)
assert not binary_search([2,3,4,5,6,7,8,9], 20)
assert not binary_search([], 20)

