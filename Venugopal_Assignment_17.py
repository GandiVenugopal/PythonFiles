class Student:
    def __init__(self):
        self.scores = []

    def input(self):
        self.scores = list(map(int, input().split()))

    def calculateTotalScore(self):
        return sum(self.scores)


# Read number of students
n = int(input())

students = []

for _ in range(n):
    s = Student()
    s.input()
    students.append(s)

kristen_score = students[0].calculateTotalScore()

count = 0
for i in range(1, n):
    if students[i].calculateTotalScore() > kristen_score:
        count += 1

print(count)
