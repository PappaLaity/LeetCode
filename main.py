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
