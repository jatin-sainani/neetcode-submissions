class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        #making a prereq_map to create vertices
        prereq_map = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereq_map[course].append(pre)


        def dfs(course, query):
            print('course:', course)
            print('query:', query)
            if query in prereq_map[course]:
                print('enter')
                return True
            for pre in prereq_map[course]:
                return dfs(pre,query)
            return False
        result = []
        for course,query in queries:
            result.append(dfs(course=course, query=query))
        
        return result
        



        