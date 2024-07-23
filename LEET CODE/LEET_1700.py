from collections import deque

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        student = deque(students)
        for i in sandwiches:
             
            if i in student:
                student.rotate(-student.index(i))
                student.popleft()
            else:
                break
                
        return len(student)