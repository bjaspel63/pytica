from pytica.gradebook import Gradebook
from pytica.attendance import Attendance
from pytica.insights import Insights
from pytica.visualizer import Visualizer
from pytica.report import Report
import matplotlib.pyplot as plt
import os
# Make sure images folder existsx
os.makedirs("images", exist_ok=True)

grades = Gradebook("scores.csv")
attendance = Attendance("attendance.csv")
insights = Insights("scores.csv")
visualizer = Visualizer("scores.csv")
report = Report("scores.csv")

# Print basic analytics
print("Class Average:", grades.class_average())
print("Top 3 Students:", grades.top_students(3))
print("Struggling Students:", insights.struggling_students(70))
print("Improving Students:", insights.improving_students())
print(attendance.absent_report("Alice"))

# Save student progress charts
for student in ["Alice", "Bob", "Charlie"]:
    row = visualizer.data[visualizer.data["Name"] == student].iloc[0, 1:]
    plt.plot(row.index, row.values, marker='o')
    plt.title(f"{student}'s Progress")
    plt.xlabel("Assessments")
    plt.ylabel("Score")
    plt.ylim(0, 100)
    plt.grid(True)
    plt.savefig(f"images/{student.lower()}_progress.png")
    plt.close()

# Save class average chart
averages = visualizer.data.iloc[:, 1:].mean()
plt.plot(averages.index, averages.values, marker='o', color='green')
plt.title("Class Average Progress")
plt.xlabel("Assessments")
plt.ylabel("Average Score")
plt.ylim(0, 100)
plt.grid(True)
plt.savefig("images/class_average_example.png")
plt.close()

# Generate reports
report.generate_excel("class_report.xlsx")
report.generate_pdf("class_report.pdf")

print("All charts saved to images/ folder!")
