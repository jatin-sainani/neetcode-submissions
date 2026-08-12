class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda interval: interval[0])
        r=1
        res = [intervals[0]]

        while r < len(intervals):
            # print(intervals)
            if (intervals[r][0]<=res[-1][1]):
                res[-1]=(
                    [min(res[-1][0],intervals[r][0]), 
                max(res[-1][1],intervals[r][1])])
            else:
                res.append(intervals[r])
            r+=1
        return(res)


        