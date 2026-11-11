from collections import deque
class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        # set up adjacency list
        # (0, 1)
        # for each course, adj list lists all courses it can take
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1
        
        queue = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                queue.append(c)
        
        done = 0
        while queue:
            node = queue.popleft()
            done += 1
            # the courses that prereq goes to
            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if done == numCourses:
            return True
        else:
            return False