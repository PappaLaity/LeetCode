'''
* leetCode.py Contain
* Objective: Two Easy - Two Medium - 1 Hard by Week 

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
        res =  str(x)
        for idx in range(len(res)//2):
            if res[idx]!=res[-(idx+1)]:
                return False
        return True
    
    def romanToInt(self, s: str) -> int:
        """
            Summary:
                This function take as input a Roman Numeral and Convert it into Integer

            Args:
                A roman numeral written using string 

            Return: 
                An Integer conversion of Roman numeral
        """
        romans = ['I','V','X','L','C','D','M']
        values = [1,5,10,50,100,500,1000]
        sum = 0
        n = len(s)
        # Go through the value of S (Recuperer sa taille)
        # for each element check the next if exist
        for i in range(n-1):
            index1 = romans.index(s[i])
            index2 = romans.index(s[i+1])
        # If the next element don't correspond to the next element in the roman list
            # we add the correspond value to the list
            if index1 >= index2:
                sum += values[romans.index(s[i])]
        # otherwise
            # We substract the next and the previous corresponding value
            # we add it in the sum numbers
            else:
                sum -= values[romans.index(s[i])]

        sum+= values[romans.index(s[n-1])]
        return sum

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
            Summary:
                    This function find in the given list of words or string item the longest common
                    value.
            Args:
                A List of string containing different words

            Return:
                    A Longest common prefix as a string
        """
        s = []
        #  Sort the list of string by len of string
        strs.sort(key = len)
        # The longest common prefix is at most the first value which have the smallest len
        item = strs[0]
        n = len(item)
        j = 0

        while j < n :
            for i in range(1,len(strs)):
                if strs[i][j] != item[j]:
                     return "".join(s)
            s.append(item[j])
            j+=1
        return "".join(s)

    def isValid(self, s: str) -> bool:
        """
            Summary: 
                    Given a string s containing only brackets determine if the input string is valid.
                    An input string is valid if:
                        Open brackets must be closed by the same type of brackets.
                        Open brackets must be closed in the correct order.
                        Every close bracket has a corresponding open bracket of the same type.
            Args:
                A string s containing just the characters '(', ')', '{', '}', '[' and ']'
            Return:
                A Boolean value meaning if the bracket in the string is well arranged

        """
        openedbracket = ["(","[","{"]
        closedbracket = [")","]","}"]
        pile = []
        # If the first character is a closed bracket return False
        if s[0] in closedbracket:
            return False
        for i in range(len(s)):
            # Check For each Character if it is in a opened bracked add it to list pile
            if s[i] in openedbracket:
                pile.append(s[i])
            # Other Wise check if the last element in pile correspond to the open bracket the actual element
            elif s[i] in closedbracket:
                if (len(pile) == 0):
                    return False
                elif openedbracket.index(pile[len(pile)-1]) == closedbracket.index(s[i]):
                    pile.pop()
                else:
                    return False
            else:
                return False # Mean the input value is not Bracket
        return len(pile) == 0
    
    def removeDuplicates(self, nums: List[int]) -> int:
        """
            Summary: 
                    Remove duplicate functions give a number of unique value in a given list
                    the first k elements in the list  should be the unique value
            Args: 
                Sorted list Of integer
            Outputs:
                    Number k of unique value
                    the given list will be modified such that the k first element will be the unique values
        """
        list_wtout_duplicate = []
        idx = []
        # for i in range(len(nums)):
        #     elt = nums[i]
        #     if elt not in list_wtout_duplicate:
        #         list_wtout_duplicate.append(elt)
        #         idx.append(i)
        list_wtout_duplicate = list(dict.fromkeys(nums))
        k = len(list_wtout_duplicate)
        for i in range(len(nums)):
            if i not in idx:
                list_wtout_duplicate.append(nums[i])
        for i in range(len(nums)):
            nums[i]=list_wtout_duplicate[i]
        return k

    def removeElement(self, nums: List[int], val: int) -> int:
        """
            Summary:
                Removes Element given a list of integer
            Args:
                A list of Integer nums
                A value val to remove in the list
            Return:
                The number k of elements in the list different to the given value
                The list k first element in the list should not have the value val

        """
        k = nums.count(val)
        for i in range(k):
            nums.remove(val)
            nums.append(val)
        return len(nums)-k
    
    def answerString(self, word: str, numFriends: int) -> str:
        """
            Summary:
            Given a string word, and an integer numFriends. word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
            All the split words are put into a box.
            Find the lexicographically largest string from the box after all the rounds are finished.
            Args:
                The word
                Number of Friends
            Returns:
                The largest lexicography 
        """
        if numFriends == 1 :
            return word
        if len(word) == numFriends:
            return max(word)
        largestLexic = ""
        n = len(word)
        k =1
        largestSize = n - numFriends + 1
        for j in range(k,largestSize+1):
            for i in range(n - j + 1):
                if word[i:i+largestSize] > largestLexic:
                    largestLexic = word[i:i+largestSize]
            
        return largestLexic
    
    def strStr(self, haystack: str, needle: str) -> int:
        """
            Summary:
                Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
                or -1 if needle is not part of haystack.
            Args:
                Two Strings haystack and needle
            Returns:
                The Index of the first occurrence of needle in haystack -1 otherwise
        """
        occur = -1 
        needle_size = len(needle)
        for i in range(len(haystack)-needle_size + 1):
            if haystack[i:i+needle_size] == needle:
                return i
        return occur