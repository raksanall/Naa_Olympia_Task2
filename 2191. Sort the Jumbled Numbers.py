# class Solution:
#     def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
#         nums.sort(key=lambda num: self.value(num, mapping))
#         return nums
    
#     def value(self, num, mapping):
#         if num == 0:
#             return mapping[0]

#         res, m = 0, 1
#         while num:
#             res += m * mapping[num % 10]
#             m *= 10
#             num //= 10
        
#         return res