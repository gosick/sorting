

class HeapSort:
    """
        heap sort with simple list
        sort using max heap
    """

    def __init__(self, input_list):
        self._input_list = input_list

    def _max_heap(self, root, heap_size):
        left = root * 2 + 1
        right = root * 2 + 2
        largest = root

        if left < heap_size and self._input_list[left] > self._input_list[largest]:
            largest = left
        
        if right < heap_size and self._input_list[right] > self._input_list[largest]:
            largest = right
        
        if largest != root:
            self._input_list[largest], self._input_list[root] = self._input_list[root], self._input_list[largest]
            self._max_heap(largest, heap_size)

    def sorting(self):
        size = len(self._input_list)
        for index in range(size // 2 - 1, -1, -1):
            self._max_heap(index, size)

        for item in range(size - 1, 0, -1):
            self._input_list[0], self._input_list[item] = self._input_list[item], self._input_list[0]
            self._max_heap(0, item)

    def get_input_list(self):
        return self._input_list
