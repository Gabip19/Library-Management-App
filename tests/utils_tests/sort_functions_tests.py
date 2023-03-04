import unittest
from utils.sort_functions import QuickSort, GnomeSort


class TestCaseSortingFunctions(unittest.TestCase):

    def setUp(self) -> None:

        self.list1 = [26616, 9263, 7473, 5994, 28274, 30703, 20652, 17415, 6583, 20497, 29364,
                      13800, 13926, 13385, 25464, 9873, 18889, 16204]

        self.list2 = [12257, 3020, 18836, 1234, 31173, 22934, 9751, 17638, 17136, 17183, 30367, 5930]

        self.list3 = [1, 1, 1, 2, 3, 4, 4, 4, 4, 5]

        self.list4 = [(12257, 4321), (3020, 421), (18836, 53211), (1234, 5321), (31173, 4211), (22934, 80241),
                      (9751, 4212), (17638, 5321), (17136, 1111), (17183, 221), (30367, 4214), (5930, 7715)]

        self.list5 = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]


    def test_QuickSort(self):

        arr = self.list1
        arr = QuickSort(arr)
        self.assertEqual(arr, sorted(self.list1))

        arr = self.list1
        arr = QuickSort(arr, reverse=True)
        self.assertEqual(arr, sorted(self.list1, reverse=True))

        arr = self.list2
        arr = QuickSort(arr)
        self.assertEqual(arr, sorted(self.list2))

        arr = self.list3
        arr = QuickSort(arr)
        self.assertEqual(arr, sorted(self.list3))

        arr = self.list3
        arr = QuickSort(arr, reverse=True)
        self.assertEqual(arr, sorted(self.list3, reverse=True))

        arr = self.list4
        arr = QuickSort(arr, key=lambda x: x[0])
        self.assertEqual(arr, sorted(self.list4, key=lambda x: x[0]))

        arr = self.list4
        arr = QuickSort(arr, key=lambda x: x[1])
        self.assertEqual(arr, [(17183, 221), (3020, 421), (17136, 1111), (31173, 4211), (9751, 4212), (30367, 4214),
                               (12257, 4321), (17638, 5321), (1234, 5321), (5930, 7715),
                               (18836, 53211), (22934, 80241)])

        arr = self.list4
        arr = QuickSort(arr, key=lambda x: x[0], reverse=True)
        self.assertEqual(arr, sorted(self.list4, key=lambda x: x[0], reverse=True))

        arr = self.list5
        arr = QuickSort(arr)
        self.assertEqual(arr, sorted(self.list5))

        arr = self.list5
        arr = QuickSort(arr, reverse=True)
        self.assertEqual(arr, self.list5)


    def test_GnomeSort(self):

        arr = self.list1
        arr = GnomeSort(arr)
        self.assertEqual(arr, sorted(self.list1))

        arr = self.list1
        arr = GnomeSort(arr, reverse=True)
        self.assertEqual(arr, sorted(self.list1, reverse=True))

        arr = self.list2
        arr = GnomeSort(arr)
        self.assertEqual(arr, sorted(self.list2))

        arr = self.list3
        arr = GnomeSort(arr)
        self.assertEqual(arr, sorted(self.list3))

        arr = self.list3
        arr = GnomeSort(arr, reverse=True)
        self.assertEqual(arr, sorted(self.list3, reverse=True))

        arr = self.list4
        arr = GnomeSort(arr, key=lambda x: x[0])
        self.assertEqual(arr, sorted(self.list4, key=lambda x: x[0]))

        arr = self.list4
        arr = GnomeSort(arr, key=lambda x: x[1])
        self.assertEqual(arr, sorted(self.list4, key=lambda x: x[1]))

        arr = self.list4
        arr = GnomeSort(arr, key=lambda x: x[0], reverse=True)
        self.assertEqual(arr, sorted(self.list4, key=lambda x: x[0], reverse=True))

        arr = self.list5
        arr = GnomeSort(arr)
        self.assertEqual(arr, sorted(self.list5))

        arr = self.list5
        arr = GnomeSort(arr, reverse=True)
        self.assertEqual(arr, self.list5)
