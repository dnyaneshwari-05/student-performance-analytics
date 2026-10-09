"""Reusable functions for the Student Performance Analytics System."""
import numpy as np
import pandas as pd

PASS_MARK = 40          
MIN_ATTENDANCE = 75     # attendance % below this is flagged


def load_data(path):
    """Read the CSV file into a Pandas DataFrame."""
    return pd.read_csv(path)


def get_subject_columns(df):
    """Subject columns = everything except the ID/details/attendance columns."""
    non_subjects = ["Student_ID", "Name", "Department", "Attendance"]
    return [col for col in df.columns if col not in non_subjects]


def assign_grade(avg):
    """Grading rule based on average marks."""
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    elif avg >= 40:
        return "E"
    return "F"


def calculate_student_metrics(df, subjects):
    """Add Total, Average, Grade, Result and Attendance_Status columns."""
    marks = df[subjects].to_numpy()                       # NumPy array of marks
    df["Total"] = np.sum(marks, axis=1)
    df["Average"] = np.round(np.mean(marks, axis=1), 2)
    df["Grade"] = [assign_grade(a) for a in df["Average"]]
    # Pass only if the student scored >= PASS_MARK in every subject
    df["Result"] = np.where(np.all(marks >= PASS_MARK, axis=1), "Pass", "Fail")
    df["Attendance_Status"] = np.where(
        df["Attendance"] >= MIN_ATTENDANCE, "OK", "Low")
    return df


def subject_analysis(df, subjects):
    """Average, highest, lowest and pass-rate for every subject."""
    rows = []
    for subject in subjects:                               
        col = df[subject].to_numpy()
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(col)), 2),
            "Highest": int(np.max(col)),
            "Lowest": int(np.min(col)),
            "Pass_%": round(float(np.mean(col >= PASS_MARK) * 100), 1),
        })
    return pd.DataFrame(rows).sort_values("Average", ascending=False)


def top_performers(df, n=5):
    """Top n students ranked by average marks."""
    return df.sort_values("Average", ascending=False).head(n)[
        ["Student_ID", "Name", "Department", "Total", "Average", "Grade"]]


def department_analysis(df):
    """Average marks and pass count per department."""
    return df.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Avg_Marks=("Average", "mean"),
        Passed=("Result", lambda r: (r == "Pass").sum()),
    ).round(2).sort_values("Avg_Marks", ascending=False)
