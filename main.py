from typing import List
import collections

class Solution:
    # 2717. Semi-Ordered Permutation
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        _nums = len(nums)
        _min = nums.index(1)
        _max = nums.index(_nums)
        if _min < _max:
            return _min +  (_nums - _max - 1)
        else:
            return _min +  (_nums - _max - 1) - 1
            

if __name__ == '__main__':
    solution = Solution()

    # 2717. Semi-Ordered Permutation
    print(solution.semiOrderedPermutation([2,4,1,3]))