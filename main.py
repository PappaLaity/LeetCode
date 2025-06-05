from leetCode import LeetCode

if __name__ == "__main__":
    leet_obj = LeetCode()

    nums = [2,7,11,15]
    target = 9

    print(f"Calling twoSum function between {nums} and {target} give: ")
    result = leet_obj.twoSum(nums,target)
    assert result == [0,1]
    print(result)

    number = 121
    # number = -10
    result = leet_obj.isPalindrome(number)
    assert result == True
    # assert result == False
    print(f"Calling Palindrome function to {number}  give {result}: ")

    number = 12121
    # number = -10
    result = leet_obj.isPalindromeV2(number)
    assert result == True
    # assert result == False
    print(f"Calling V2 of Palindrome function to {number}  give {result}: ")

    # Numeral Roman to Integer
    roman = "MCMXCIV"
    intValue = leet_obj.romanToInt(roman)
    print(f"The Equivalent value of {roman} in Integer gives {intValue}: ")
    
    # The longest Common prefix in a list
    strs = ["planting", "planter", "plants", "planted", "plantation"]
    prefix = leet_obj.longestCommonPrefix(strs)

    print(f"The Longest common prefix for {strs} is: {prefix} ")

    # Is Valid Function  
    s = "(]"
    result = leet_obj.isValid(s)
    assert result == False
    
    # Remove duplicates values in a given list
    nums  = [1,1,2]
    expect = [1,2]
    k = leet_obj.removeDuplicates(nums)
    assert k == 2
    assert expect == nums[:k]

    # Remove Element and Occurence in a given list

    nums,val = [0,1,2,2,3,0,4,2], 2
    k = leet_obj.removeElement(nums,val)
    expectedNums = nums[:k]
    assert val not in expectedNums

    # answerString
    s= "aann"
    numFriends =2
    result = leet_obj.answerString(s,numFriends)
    print("Result: ",result)
    assert result == "nn"