# Student Performance Analytics System

A Python data-analysis project using **NumPy** and **Pandas** that analyses student marks and attendance.

## Files
| File | Purpose |
|---|---|
| `main.py` | Runs the analysis and prints the report |
| `functions.py` | Reusable calculation/processing functions |
| `students.csv` | Dataset (20 students, 5 subjects + attendance) |
| `results.csv` | Generated output with totals, grades, results |

## How to run
```
pip install numpy pandas
python main.py
```

## Rules used
- **Grades (by average):** A+ >= 90, A >= 80, B >= 70, C >= 60, D >= 50, E >= 40, F < 40
- **Pass:** at least 40 marks in every subject, otherwise Fail
- **Low attendance:** below 75%

## Features
Total/average per student, grades, pass/fail, class average, highest/lowest, grade distribution, subject-wise analysis, top 5 students, department analysis, at-risk students.
