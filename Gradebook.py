last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["Physics", "Calculus", "Poetry", "History"]
subjects.append("Computer Science")

grades = [98, 98, 85, 88]
grades.append(100)

gradebook = zip(subjects, grades)

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
