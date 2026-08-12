class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prereqMap = [[] for _ in range(numCourses)]
        visiting = set()
        visited = set()
        res = []

        for course, pre in prerequisites:
            prereqMap[course].append(pre)

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)

            for pre in prereqMap[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            visited.add(course)
            res.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res