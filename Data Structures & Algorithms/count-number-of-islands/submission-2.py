class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

      rows,cols = len(grid), len(grid[0])

      visited = []
      island = 0
      directions = [[0,1],[1,0],[0,-1],[-1,0]] #up,right,down,left


      def bfs(r,c):

        q = collections.deque()
        q.append((r,c))
        visited.append((r,c))

        while q:
            row,col = q.popleft()
            visited.append((row,col))

            for dr,dc in directions:
                nr,nc = row+dr, col+dc
                if nr in range(rows) and nc in range(cols):
                    neighbor = grid[nr][nc]
                    if neighbor == '1' and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.append(((nr,nc)))


      for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r,c) not in visited:
                print('enter bfs for',r,c)
                bfs(r,c)
                island +=1
                print(island)
      return island

      

