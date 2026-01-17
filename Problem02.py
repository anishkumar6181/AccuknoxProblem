import requests
import matplotlib.pyplot as plt

# Example API endpoint
api_url = "https://example.com/api/student_scores"

# fecthing the data from the API
response = requests.get(api_url)
students = response.json()

# Separating names and scores
student_names = []
student_scores = []

for student in students:
    student_names.append(student["name"])
    student_scores.append(student["score"])

# Calculating average score
average_score = sum(student_scores) / len(student_scores)
print("Average Score:", average_score)

# Creating the bar chart
plt.bar(student_names, student_scores)
plt.axhline(average_score, linestyle="--", label="Average Score")

plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Test Scores")
plt.legend()
plt.show()
