"""Student Performance Analytics System - main program."""
import numpy as np
import functions as fn


def line(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main(): 
    df = fn.load_data("students.csv")
    subjects = fn.get_subject_columns(df)

    line("1. DATASET OVERVIEW")
    print(f"Records : {df.shape[0]}")
    print(f"Columns : {list(df.columns)}")
    print(f"Missing values: {int(df.isna().sum().sum())}")
    print(df.head())
 
    df = fn.calculate_student_metrics(df, subjects)

    line("2. STUDENT REPORT")
    print(df[["Student_ID", "Name", "Total", "Average", "Grade", "Result",
              "Attendance_Status"]].to_string(index=False))
 
    line("3. CLASS SUMMARY")
    avg = df["Average"].to_numpy()
    best = df.loc[df["Average"].idxmax()]
    worst = df.loc[df["Average"].idxmin()]
    passed = (df["Result"] == "Pass").sum()
    failed = len(df) - passed
    print(f"Overall class average : {np.mean(avg):.2f}")
    print(f"Median average        : {np.median(avg):.2f}")
    print(f"Standard deviation    : {np.std(avg):.2f}")
    print(f"Highest average       : {best['Name']} ({best['Average']})")
    print(f"Lowest average        : {worst['Name']} ({worst['Average']})")
    print(f"Passed / Failed       : {passed} / {failed}  "
          f"(pass rate {passed / len(df) * 100:.1f}%)")

    line("4. GRADE DISTRIBUTION")
    counts = df["Grade"].value_counts()
    for grade in ["A+", "A", "B", "C", "D", "E", "F"]:    # loop in fixed order
        n = counts.get(grade, 0)
        print(f"{grade:>2} | {'#' * n} {n}")

    line("5. SUBJECT-WISE PERFORMANCE")
    sub = fn.subject_analysis(df, subjects)
    print(sub.to_string(index=False))
    print(f"\nBest subject  : {sub.iloc[0]['Subject']} "
          f"(avg {sub.iloc[0]['Average']})")
    print(f"Weakest subject: {sub.iloc[-1]['Subject']} "
          f"(avg {sub.iloc[-1]['Average']})")

    line("6. TOP 5 PERFORMERS")
    print(fn.top_performers(df).to_string(index=False))

    line("7. DEPARTMENT-WISE PERFORMANCE")
    print(fn.department_analysis(df))

    line("8. STUDENTS NEEDING ATTENTION")
    at_risk = df[(df["Result"] == "Fail") | (df["Attendance_Status"] == "Low")]
    print(at_risk[["Name", "Average", "Result", "Attendance"]]
          .to_string(index=False))
 
    df.to_csv("results.csv", index=False)
    print("\nFull results saved to results.csv")


if __name__ == "__main__":
    main()
