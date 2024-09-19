class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)-1):
                if nums1[i]==nums2[j]:
                    return nums1[i]
        return -1
       
nums1=[1,2]
nums2=[2,3]
x=Solution()
print(x.getCommon(nums1,nums2))