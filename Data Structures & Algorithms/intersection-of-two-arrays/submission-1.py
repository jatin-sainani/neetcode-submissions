class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # res = set()
        # for i in nums1:
        #     for j in nums2:
        #         if i==j:
        #             res.add(i)
        
        # return(list(res))

        res = []
        set1 = set(nums1)
        set2 = set(nums2)
        
        for num in set1:
            if num in set2:
                res.append(num)
        
        return res
        


        