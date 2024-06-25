# class Solution:
#     def findMinArrowShots(self, points: List[List[int]]) -> int:

#         if not points:
#             return 0

#         for i in range(len(points)):
#             for j in range(0, len(points) - i - 1):
#                 if points[j][1] > points[j + 1][1]:
#                     points[j], points[j + 1] = points[j + 1], points[j]

#         arrows = 1
#         end = points[0][1]
        
#         for i in range(1, len(points)):
#             if points[i][0] > end:
#                 arrows += 1
#                 end = points[i][1]
                
#         return arrows
