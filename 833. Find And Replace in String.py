# class Solution:
#     def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
#         hashmap={}
#         for i in range(len(indices)):
#             l=len(sources[i])-1
#             if i+l>=len(s):
#                 continue
#             index=indices[i]
#             string=s[index:index+l+1]
#             if string==sources[i]:
#                 hashmap[index]=(sources[i],targets[i])
#         ans=[]
#         i=0
#         while i<len(s):
#             if i not in hashmap:
#                 ans.append(s[i])
#                 i+=1
#             else:
#                 src,trg=hashmap[i]
#                 i=i+len(src)
#                 ans.append(trg)
#         return "".join(ans)



        