class Solution(object):
    def findOriginalArray(self, changed):
        original = []
        a = Counter(changed)
        for num in sorted(changed):
            if not a[num]:
                continue
            double = 2 * num
            if not a[double]:
                return []
            original.append(num)
            a[num] -= 1
            a[double] -= 1
        return original if all(not a[num] for num in changed) else []
