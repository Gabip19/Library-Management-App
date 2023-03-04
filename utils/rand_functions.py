import random
import string
from random import randint


def randomword(length):
    """
    Genereaza un cuvant aleatoriu
    :param length: lungimea cuvantului ce va fi generat
    :type length: int
    :return: cuvantul generat cu litere aleatorii
    :rtype: str
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def randomcnp():
    """
    Genereaza un CNP cu cifre aleatorii
    :return: CNP-ul creat
    :rtype: str
    """
    digit_list = []
    for i in range(13):
        digit_list += str(randint(0, 9))
    return ''.join(digit_list)
