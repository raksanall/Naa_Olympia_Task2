# class Solution:
#     def customSortString(self, order: str, s: str) -> str:
#         l=len(s)
#         ans=''
#         for i in order:
#             if i in s:
#                 c=s.count(i)
#                 ans+=(i)*c
#         for i in s:
#             if i not in ans:
#                 c=s.count(i)
#                 ans+=(i)*c
#         return ans