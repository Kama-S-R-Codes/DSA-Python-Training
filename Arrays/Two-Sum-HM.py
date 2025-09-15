# Problem: Two Sum 
# Problem: Given an array of numbers, return indices of the two numbers that add up to a target.
# Approach 2: HashMap (Dictionary in Python):
#   - For each number, we calculate its "complement" = target - number.
#   - If this complement has already been seen, we found the answer.
#   - Otherwise, store the number with its index in a dictionary for future checks.
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Teaching Note: Starting point before introducing optimized approach of HashMap
# Time Complexity: O(n)   (one pass through array, O(1) lookups)
# Space Complexity: O(n)  (store seen numbers in dictionary)

class Solution:
    def Two_Sum_HM(self,nums:list[int],target:int)->list[int]:
        Val_Map={} # HashMap to store number → index
        for i, n in enumerate(nums):
            Sub_Val=target-n
            # Step 1: Check if complement is already seen
            if Sub_Val in Val_Map: # Check whether the subtracted value is in the Hash Map
                return [Val_Map[Sub_Val],i] 
            # Step 2: Otherwise, store this number
            Val_Map[n]=i
        return None # If no solution (though problem says one always exists)

nums=[2,7,11,15]
target=17
soln=Solution()
res=soln.Two_Sum_HM(nums,target)
print("The 2 indices' value that gives the target value are: ",res)   