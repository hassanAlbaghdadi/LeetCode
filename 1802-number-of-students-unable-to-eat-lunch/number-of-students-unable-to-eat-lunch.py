class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        counter = 0
        while counter < len(students):
            if students[0] == sandwiches[0]:
                sandwiches.popleft()
                counter = 0
            else:
                students.append(students[0])
                counter += 1
            students.popleft()
        return counter