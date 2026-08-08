class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
            
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for nextCourse in graph[course]:
                indegree[nextCourse] -= 1

                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)

        if len(order) == numCourses:
            return order

        return []