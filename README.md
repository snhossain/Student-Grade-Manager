# Student Grade Manager

A Python project that organises student marks and generates individual and class summaries.

## Features

- Calculates each student's average, highest and lowest marks.
- Counts passed and failed assessments.
- Assigns an illustrative classification based on average marks.
- Summarises class performance and classification distribution.
- Validates marks and handles students with no recorded marks.

## Requirements

- Python 3
- No external libraries required.

## Getting Started

Save the code as `student_grade_manager.py`, then run:

```bash
python student_grade_manager.py
```

Edit the `students` dictionary to analyse your own data:

```python
students = {
    "Shahriyar": [72, 68, 81, 59],
    "Ali": [45, 38, 52, 61],
    "Sara": [85, 91, 78, 88],
    "Omar": [],
}
```

## Usage

```python
result = student_records(students, pass_mark=40)

print(result["students"])
print(result["summary"])
print(result["grade_distribution"])
```

The function returns three sections:

| Section | Contents |
|---|---|
| `students` | Individual marks, statistics, pass/fail counts and classification |
| `summary` | Student count, mark count, overall average, highest/lowest marks and pass/fail totals |
| `grade_distribution` | Number of students in each classification |

## Example Student Record

For marks `[72, 68, 81, 59]`:

```python
{
    "marks": [72, 68, 81, 59],
    "average": 70.0,
    "highest": 81,
    "lowest": 59,
    "passed": 4,
    "failed": 0,
    "classification": "First"
}
```

## Classification Bands

| Average | Classification |
|---|---|
| 70–100 | First |
| 60–below 70 | 2:1 |
| 50–below 60 | 2:2 |
| 40–below 50 | Third |
| Below 40 | Fail |

These are illustrative bands, not an official university degree-classification calculation. All assessments have equal weight.

Changing `pass_mark` affects assessment pass/fail counts; it does not change the classification bands.

## Input Validation

- Marks must be integers or floats between 0 and 100.
- Boolean values and invalid marks raise a `ValueError`.
- Students with empty mark lists receive `None` for numerical summaries and a `"No marks"` classification.
- An empty dataset returns zero counts and `None` for unavailable statistics.

The class average is calculated across all recorded assessment marks. Students with more assessments therefore contribute more marks to this average.

## Skills Practised

- Functions, loops and conditional logic
- Lists and dictionaries
- Numerical calculations and aggregation
- Input validation and handling edge cases
- Structured reporting

## Limitations

- Records are supplied directly in the code.
- Data is not saved between runs.
- Assessment weighting and CSV import/export are not implemented.

## Author

Shahriyar Hossain
