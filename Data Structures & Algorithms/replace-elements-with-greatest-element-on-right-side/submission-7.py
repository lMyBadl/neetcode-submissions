class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        running_max = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = running_max
            running_max = max(running_max, temp)

        return arr