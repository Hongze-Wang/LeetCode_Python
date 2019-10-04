# 167. Two Sum II - Input array is sorted

# two pointers way

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        i, j = 0, size-1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return [i+1, j+1]

# binary search theoretically O(logn)
# because the for loop very slow in practice
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, h = i+1, len(numbers)-1
            temp = target - numbers[i]
            while l <= h:
                mid = l + (h-l) // 2
                if numbers[mid] == temp:
                    return [i+1, mid+1]
                elif numbers[mid] > temp:
                    h = mid - 1
                else:
                    l = mid + 1