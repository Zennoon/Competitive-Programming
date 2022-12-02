class Solution:
    def select(self, arr, i):
        return arr[i]

    def selectionSort(self, arr, n):
        for i in range(n):
            min_idx = arr.index(self.select(arr, i))
            for j in range(i + 1, n):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
