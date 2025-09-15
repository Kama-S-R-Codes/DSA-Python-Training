# Problem: Two Sum 
# Problem: Given an array of numbers, return indices of the two numbers that add up to a target.
# Approach 1: Brute Force:
    # Checking every pair of numbers
    # Check if their sum == target
# Test Cases: [2,7,11,15]
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Teaching Note: Starting point before introducing optimized approach of HashMap
class Solution:
    def Twosum(self,nums:list[int], target:int)->list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return()
nums=[2,7,11,15]
target=9
solution=Solution() #Object Creation
result=solution.Twosum(nums,target) #Call the function using the object
print("The indices are: ",result)