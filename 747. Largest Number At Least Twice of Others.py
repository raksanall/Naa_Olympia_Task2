# class Solution:
#     def dominantIndex(self, nums: List[int]) -> int:
#         largest=max(nums)
#         indexof=nums.index(largest)
#         nums.remove(largest)
#         for i in range(len(nums)):
#             if nums[i]>largest/2:
#                 return -1
#         return indexof


        