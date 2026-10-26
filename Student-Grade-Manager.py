def student_records(students, pass_mark=40):
    records = {}
    all_marks = []

    for name, marks in students.items():
        marks = list(marks)

        if any(
            isinstance(mark, bool)
            or not isinstance(mark, (int, float))
            or not 0 <= mark <= 100
            for mark in marks
        ):
            raise ValueError(f"Invalid marks for {name}: use numbers from 0 to 100.")

        if not marks:
            records[name] = {
                "marks": [],
                "average": None,
                "highest": None,
                "lowest": None,
                "passed": 0,
                "failed": 0,
                "classification": "No marks",
            }
            continue

        average = sum(marks) / len(marks)
        passed = sum(mark >= pass_mark for mark in marks)

        if average >= 70:
            classification = "First"
        elif average >= 60:
            classification = "2:1"
        elif average >= 50:
            classification = "2:2"
        elif average >= 40:
            classification = "Third"
        else:
            classification = "Fail"

        records[name] = {
            "marks": marks,
            "average": round(average, 2),
            "highest": max(marks),
            "lowest": min(marks),
            "passed": passed,
            "failed": len(marks) - passed,
            "classification": classification,
        }

        all_marks.extend(marks)

    distribution = {
        "First": 0,
        "2:1": 0,
        "2:2": 0,
        "Third": 0,
        "Fail": 0,
        "No marks": 0,
    }

    for record in records.values():
        distribution[record["classification"]] += 1

    return {
        "students": records,
        "summary": {
            "student_count": len(students),
            "mark_count": len(all_marks),
            "average_mark": (
                round(sum(all_marks) / len(all_marks), 2)
                if all_marks else None
            ),
            "highest_mark": max(all_marks) if all_marks else None,
            "lowest_mark": min(all_marks) if all_marks else None,
            "passed_marks": sum(mark >= pass_mark for mark in all_marks),
            "failed_marks": sum(mark < pass_mark for mark in all_marks),
        },
        "grade_distribution": distribution,
    }


# Example student data
students = {
    "Shahriyar": [72, 68, 81, 59],
    "Nuh": [45, 38, 52, 61],
    "Yeah": [85, 91, 78, 88],
    "Thushan": [],
}

result = student_records(students)

for name, record in result["students"].items():
    print(f"\n{name}")
    for key, value in record.items():
        print(f"  {key}: {value}")

print("\nClass summary:")
for key, value in result["summary"].items():
    print(f"  {key}: {value}")

print("\nGrade distribution:")
for grade, count in result["grade_distribution"].items():
    print(f"  {grade}: {count}")
