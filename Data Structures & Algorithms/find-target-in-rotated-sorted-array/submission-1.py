class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if target not in nums:
            return -1
        
        return nums.index(target)

        # copy = sorted(nums)
        # rotation = nums.index(copy[0])
        # return rotation
        # print(nums)
        # print(copy)
        # print(rotation)
        
        # l,r =0, len(nums)
        # mid = r // 2

        # while mid!=target:
        #     mid = (l+r) // 2
        #     if l>mid:
        #         r=mid
        #     if mid>r:
        #         l=mid
        
        