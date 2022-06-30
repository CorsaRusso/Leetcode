class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for i in prerequisites:
            preMap[i[0]].append(i[1])
        # print(preMap)
        def dfs(crs, visited):
            # print("___")
            # print("CRS:",crs)
            # print("preMap:", preMap)
            # print("Visited:", visited)
            if crs in visited:
                # print("visited")
                return False
            visited.add(crs)
            if(not preMap[crs]):
                # print("emptied")
                return True

            for i in preMap[crs]:
                visited2 = visited.copy()
                if (not dfs(i, visited2)):
                    return False
            preMap[crs] = []
            
            return True
        for i in prerequisites:
            # print("LOOP BEGIN")
            visited = set()
            if(not dfs(i[0], visited)):
                return False
            # print("LOOP END")
        return True