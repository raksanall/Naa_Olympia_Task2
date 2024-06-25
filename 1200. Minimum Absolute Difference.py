# class Solution:
#     def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
#         arrList=[]
#         arr.sort()
#         diff=abs(arr[1]-arr[0])
#         for i in range(len(arr)-1):
#             current_diff = arr[i + 1] - arr[i]
#             if current_diff < diff:
#                 diff = current_diff
#                 arrList=[[arr[i],arr[i+1]]]
#             elif current_diff==diff:
#                 arrList.append([arr[i],arr[i+1]])
#         return arrList