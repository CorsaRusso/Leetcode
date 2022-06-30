class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        visited = set()
        for i in range(numCourses):
            preMap[i] = []
        for i in prerequisites:
            preMap[i[0]].append(i[1])
        # print(preMap)
        def dfs(crs):
            # print("___")
            # print("CRS:",crs)
            # print("preMap:", preMap)
            # print("Visited:", visited)
            if crs in visited:
                # print("visited")
                return False
            if(not preMap[crs]):
                # print("emptied")
                return True
            visited.add(crs)
            for i in preMap[crs]:
                if (not dfs(i)):
                    return False

            visited.remove(crs)
            preMap[crs] = []
            
            return True
        for i in prerequisites:
            # print("LOOP BEGIN")
            if(not dfs(i[0])):
                return False
            # print("LOOP END")
        return True