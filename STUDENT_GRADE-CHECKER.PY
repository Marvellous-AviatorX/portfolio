# 🧪📊 Student Grades Checker
# This program asks how many students took a test,
# collects their scores, and prints their grades.

student_number = int(input("🧑‍🎓 How many students took the test? \n"))

for a in range(student_number):
    student_score = int(input("✏ Enter score for Student " + str(a + 1) + ": "))

    if student_score >= 90:
        print("🏅 Grade: A – Excellent 🌟 \n")
    if student_score >= 80 and student_score <=89:
        print("🎖 Grade: B – Great job \n")
    if student_score >= 70 and student_score <=79:
        print("✅ Grade: C – Good effort \n")
    if student_score <70:
        print("❌ Fail – Keep trying 💪 \n")