'''
* leetCode.py Contain

'''

from typing import List


class LeetCode():
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            Summary:
                        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
                        Assume that each input would have exactly one solution, we may not use the same element twice.
            Args:
                nums (list[int]): A List of Integers in wich we search two values such that there sum equal to target 
                target (int) : A target value
        
            Returns: 
                    A list of two index which the sum of the corresponding value in the nums list is equal to target 
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
    
    
    def isPalindrome(self, x: int) -> bool:
        """
            Summary:
                        Given an integer, we may see if it is a palindrome or not. 
                        A value is a palindrome if It reads the same backwards as forwards
            Args:
                x (int) : The value to see if it is a Palindrom
            Returns: 
                    A boolean Response about the nature of x (True if is palindrome, False if not) 
        """
        if x < 0 :
            return False
        reversed = int(str(x)[::-1])
        return x == reversed



    def isPalindromeV2(self,x:int)->bool:
        """
            Summary:
                        Given an integer, we may see if it is a palindrome or not. 
                        A value is a palindrome if It reads the same backwards as forwards
                        For this function we resolve the problem without slicing
            Args:
                x (int) : The value to see if it is a Palindrom
            Returns: 
                    A boolean Response about the nature of x (True if is palindrome, False if not) 
        """
        if x < 0 :
            return False
        res = list(map(int, str(x)))
        for i in range(len(res)//2):
            if res[i]!=res[-(i+1)]:
                return False
        return True


