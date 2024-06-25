# class Solution:
#     def minMoves2(self, nums: List[int]) -> int:
#         nums.sort()
#         mid_num = nums[len(nums) // 2]       
#         result = 0
#         for num in nums:
#             result += abs(mid_num - num)
        
#         return result