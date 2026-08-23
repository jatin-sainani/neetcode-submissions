class MedianFinder:

    def __init__(self):
        self.left, self.right = [] , []
        

    def addNum(self, num: int) -> None:
        #both should be equal
        # if num is bigger than right's smallest then push to right
        # else push to left

        # if left > right + 1:
        # pop right min and append left

        if (self.right and num > self.right[0]):
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, num * -1)
        
        if len(self.right) + 1 < len(self.left):
            left_max = heapq.heappop(self.left)
            heapq.heappush(self.right, left_max * -1)

        elif len(self.right) > len(self.left) + 1:
            right_min = heapq.heappop(self.right)
            heapq.heappush(self.left, right_min * -1)
        #Maybe reverse as well

        # print("left", self.left)
        # print("right", self.right)
        

    def findMedian(self) -> float:
        l1, l2 = len(self.left), len(self.right)
        if l1 == l2:
            sum = (self.left[0] * -1) + (self.right[0])
            return sum/2
        elif l1>l2:
            return self.left[0] * -1
        elif l2>l1:
            return self.right[0]
            

        
        