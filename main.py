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
