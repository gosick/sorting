import unittest
import src.heapsort as heapsort

class TestHeapSort(unittest.TestCase):

    def test_fixed_case(self):

        origin = [30, 20, 20, 21, 15, 1, 10, 5]
        print("input:", origin)
        h = heapsort.HeapSort(origin)
        h.sorting()
        output = h.get_input_list()
        print("output:", output)
        self.assertEqual(origin, output)

    def test_random_case(self):

        def generate_random(nums=100, max_int=150):
            output_list = []
            from random import randint
            for _ in range(nums):
                ele = randint(0, max_int)
                output_list.append(ele)
            return output_list

        origin = generate_random()
        print("input:", origin)
        h = heapsort.HeapSort(origin)
        h.sorting()
        output = h.get_input_list()
        print("output:", output)
        self.assertEqual(origin, output)


if __name__ == '__main__':
    unittest.main()
