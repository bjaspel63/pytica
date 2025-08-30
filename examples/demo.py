from pytica.gradebook import Gradebook
from pytica.attendance import Attendance
from pytica.insights import Insights
from pytica.visualizer import Visualizer
from pytica.report import Report

grades = Gradebook("examples/scores.csv")
attendance = Attendance("examples/attendance.csv")
insights = Insights("examples/scores.csv")
visualizer = Visualizer("examples/scores.csv")
report = Report("examples/scores.csv")

print("Class Average:", grades.class_average())
print("Top 3 Students:", grades.top_students(3))
print("Struggling Students:", insights.struggling_students(70))
print("Improving Students:", insights.improving_students())
print(attendance.absent_report("Alice"))

visualizer.plot_student_progress("Alice")
visualizer.plot_class_average()

report.generate_excel("examples/class_report.xlsx")
report.generate_pdf("examples/class_report.pdf")
