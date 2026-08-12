class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        shorten = 0
        for index, value in enumerate(nums):
            if value == val:
                shorten+=1
                nums[index] = sys.maxsize
        nums.sort()
        print(nums)
        return(len(nums)-shorten)
        