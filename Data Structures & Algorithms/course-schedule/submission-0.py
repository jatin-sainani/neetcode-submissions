class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        ##data structures
        preMap = {i:[] for i in range(numCourses)}
        visiting = set()

        ##creating premap
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        print("PreMap", preMap)


        def dfs(course):

            if course in visiting:
                False
            
            if preMap[course] == []:
                return True

            visiting.add(course)
            for pre in preMap[course]:
                if pre in visiting:
                    return False
                if not dfs(pre):
                    return False

            visiting.remove(course)
            return True

        ##running dfs for all courses
        for j in range(numCourses):
            if not dfs(j):
                return False
        return True
            

                
        