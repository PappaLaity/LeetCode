'''
* leetCode.py Contain

'''

from typing import List


class LeetCode():
    pass
    # def __init__(self):
    #     pass
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]


