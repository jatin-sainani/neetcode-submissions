class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        rotten = collections.deque()
        minutes = 0
        fresh = 0

        # get all the rotten fruits
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                if grid[r][c] == 1:
                    fresh+=1
        print("pre")
        print(fresh)
        print(rotten)
        print("___")
        if rotten == None:
            return -1

                #visited_rotten.append((r,c))
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while rotten and fresh>0:
            level_size = len(rotten)
            for j in range(level_size):
                rr, rc = rotten.popleft() 
                for dr, dc in directions:
                    if((rr+dr) in range(0,rows) and
                    (rc+dc) in range(0,cols) and
                    grid[rr+dr][rc+dc]==1):
                        grid[rr+dr][rc+dc] = 2
                        rotten.append((rr+dr,rc+dc))
                        fresh-=1
            minutes+=1
        print("post")
        print(fresh)
        print(rotten)
        print("___")
        return minutes if fresh ==0 else -1




        

        