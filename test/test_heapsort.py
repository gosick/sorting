import unittest
import src.heapsort as heapsort

class TestHeapSort(unittest.TestCase):

    def test_fixed_case_with_max_heap(self):
        import copy
        origin = [30, 20, 20, 21, 15, 1, 10, 5]
        input = copy.copy(origin)
        print("input:", input)
        h = heapsort.HeapSort(input)
        h.max_sorting()
        output = h.get_input_list()
        print("output:", output)
        self.assertFalse(origin == output)
        # sort from small to large
        origin.sort()
        self.assertTrue(origin == output)

    def test_fixed_case_with_min_heap(self):
        import copy
        origin = [30, 20, 20, 21, 15, 1, 10, 5]
        input = copy.copy(origin)
        print("input:", input)
        h = heapsort.HeapSort(input)
        h.min_sorting()
        output = h.get_input_list()
        print("output:", output)
        self.assertFalse(origin == output)
        # sort from large to small
        origin.sort(reverse=True)
        self.assertTrue(origin == output)

    def generate_random(self, nums=100, max_int=150):
        output_list = []
        from random import randint
        for _ in range(nums):
            ele = randint(0, max_int)
            output_list.append(ele)
        return output_list

    def test_random_case_with_max_heap(self):
        import copy
        origin = self.generate_random()
        input = copy.copy(origin)
        print("input:", input)
        h = heapsort.HeapSort(input)
        h.max_sorting()
        output = h.get_input_list()
        print("output:", output)
        self.assertFalse(origin == output)
        # sort from small to large
        origin.sort()
        self.assertTrue(origin == output)

    def test_random_case_with_min_heap(self):
        import copy
        origin = self.generate_random()
        input = copy.copy(origin)
        print("input:", input)
        h = heapsort.HeapSort(input)
        h.min_sorting()
        output = h.get_input_list()
        print("output:", output)
        self.assertFalse(origin == output)
        # sort from large to small
        origin.sort(reverse=True)
        self.assertTrue(origin == output)


if __name__ == '__main__':
    unittest.main()
