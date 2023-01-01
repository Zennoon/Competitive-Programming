class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        size = len(arr)
        ks = []
        while size > 1:
            index = arr.index(max(arr[:size]))
            if index != size - 1:
                self.flip(arr, index)
                ks.append(index + 1)
                self.flip(arr, size - 1)
                ks.append(size)
            size -= 1
        if 1 in ks:
            ks.remove(1)
        return ks
    def flip(self, arr, i):
        start = 0
        while start < i:
            temp = arr[start]
            arr[start] = arr[i]
            arr[i] = temp
            start += 1
            i -= 1
