from random import randint


def Sort(arr, key=lambda x: x, reverse=False, cmp=lambda x, y: x >= y):
    """
    Sorteaza o lista/dictionar de elemente
    :param arr: lista/dictionarul ce urmeaza a fi sortat
    :type arr: list / dict
    :param key: (optional) cheia in functie de care se va sorta lista
           (default: elementul efectiv)
    :type key: function
    :param reverse: (optional) precizeaza daca lista se va sorta descrescator
           in functie de cheia data
           (default: False)
    :type reverse: bool
    :param cmp
    :return: o lista sortata in functie de conditiile stabilite
    :rtype: list
    """
    # choice = randint(0, 5)
    choice = 0
    if choice % 2 == 0:
        print("\nSortat cu QuickSort\n")
        arr = QuickSort(arr, key, reverse, cmp)
    else:
        print("\nSortat cu GnomeSort\n")
        arr = GnomeSort(arr, key, reverse)
    return arr


def QuickSort(arr, key=lambda x: x, reverse=False, cmp=lambda x, y: x >= y):
    """
    Sorteaza o lista/dictionar de elemente utilizand Quick Sort
    :param arr: lista/dictionarul ce urmeaza a fi sortat
    :type arr: list / dict
    :param key: (optional) cheia in functie de care se va sorta lista
           (default: elementul efectiv)
    :type key: function
    :param reverse: (optional) precizeaza daca lista se va sorta descrescator
           in functie de cheia data
           (default: False)
    :type reverse: bool
    :param cmp
    :return: o lista sortata in functie de conditiile stabilite
    :rtype: list
    """
    arr = list(arr)
    quick_sort(arr, 0, len(arr) - 1, key, cmp)
    if reverse:
        arr.reverse()
        return arr
    else:
        return arr


def partition(arr, start, end, key, cmp):
    """
    Functia responsabila cu crearea partitiilor aranjate in functie de un pivot
    :param arr: lista pentru care se modifica ordinea elementelor in functie
           de un pivot ales mereu ca fiind primul element
    :type arr: list
    :param start: index-ul elementului de start
    :type start: int
    :param end: index-ul elementului final
    :type end: int
    :param key: cheia in functie de care se va sorta lista
           (default: elementul efectiv)
    :type key: function
    :param cmp
    :return: pozitia elementului pivot in urma partitiei
    :rtype: int
    """
    pivot = arr[start]
    low = start + 1
    high = end

    while True:

        while low <= high and cmp(key(arr[high]), key(pivot)):
            high -= 1

        while low <= high and not cmp(key(arr[low]), key(pivot)):
            low += 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]
    return high


def quick_sort(arr, start, end, key, cmp):
    """
    Functia responsabila cu apelarea recursiva a quicksortul-ui pe ramuri
    :param arr: lista ce se va sorta
    :type arr: list
    :param start: index-ul elementului de start
    :type start: int
    :param end: index-ul elementului final
    :type end: int
    :param key: cheia in functie de care se va sorta lista
           (default: elementul efectiv)
    :type key: function
    :param cmp
    """
    if start >= end:
        return

    p = partition(arr, start, end, key, cmp)
    quick_sort(arr, start, p - 1, key, cmp)
    quick_sort(arr, p + 1, end, key, cmp)


def GnomeSort(arr, key=lambda x: x, reverse=False):
    """
    Functia coordonator pentru Gnome Sort
    :param arr: lista/dictionarul ce urmeaza a fi sortat
    :type arr: list / dict
    :param key: (optional) cheia in functie de care se va sorta lista
           (default: elementul efectiv)
    :type key: function
    :param reverse: (optional) precizeaza daca lista se va sorta descrescator
           in functie de cheia data
           (default: False)
    :type reverse: bool
    :return: o lista sortata in functie de conditiile stabilite
    :rtype: list
    """
    arr = list(arr)
    gnome_sort(arr, key)
    if reverse:
        arr.reverse()
        return arr
    else:
        return arr


def gnome_sort(arr, key):
    """
    Sorteaza o lista data utilizand Gnome Sort
    :param arr: lista ce va fi sortata
    :type arr: list
    :param key: cheia in functie de care se va sorta lista
           (default: elementul efectiv)
    :type key: function
    """
    poz = 0
    while poz < len(arr):
        if poz == 0 or key(arr[poz]) >= key(arr[poz - 1]):
            poz += 1
        else:
            arr[poz], arr[poz - 1] = arr[poz - 1], arr[poz]
            poz -= 1


# def cmp_two_pairs(item1, item2):
#     if item1[0] > item2[0]:
#         return True
#     elif item1[0] == item2[0]:
#         if item1[1] >= item2[1]:
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# array = [('a', 1), ('b', 3), ('b', 0), ('b', 1), ('a', 2), ('b', 2)]
# array = QuickSort(array, cmp=cmp_two_pairs)
# print(array)
