class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        unique_num = set()

        for num in nums:
            if num not in unique_num:
                unique_num.add(num)
            else:
                return True

        return False
