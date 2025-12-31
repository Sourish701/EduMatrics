

# Importing all your modules
import funcsem       # File 4: The Data Entry & Average Logic
import funchighpsem     # File 2: Semester-wise Toppers
import funchighpsub     # File 3: Subject-wise Highest Marks
import funcanalysis    # File 1: Full Student Performance Analysis

def main():
    # HEADER
    print("="*60)
    print("       WELCOME TO THE EDUMETRICS CONTROL CENTER")
    print("="*60)

    try:
        # STEP 1: DATA ENTRY & AVERAGE CALCULATION (File 4)
        print("\n[SYSTEM] Starting Data Entry Module...")
        i, i1, i2, i3 = funcsem.sem_marks()

        # STEP 2: SEMESTER HIGHEST SCORERS (File 2)
        print("="*60)
        print("       TOPPERS IN EACH SEMESTER")
        print("="*60)
        print("\n[SYSTEM] Calculating Semester-wise Toppers...")
        funchighpsem.highest_in_1stsem(i)
        funchighpsem.highest_in_2ndsem(i1)
        funchighpsem.highest_in_3rdsem(i2)
        funchighpsem.highest_in_4thsem(i3)

        # STEP 3: SUBJECT-WISE HIGHEST MARKS (File 3)
        print("="*60)
        print("       TOPPERS IN EACH SUBJECT")
        print("="*60)
        print("\n[SYSTEM] Calculating Subject-wise Highest Marks...")
        funchighpsub.find_highest_per_subject(i, i1, i2, i3)
        # STEP 4: FULL STUDENT PERFORMANCE ANALYSIS (File 1)
        print("\n[SYSTEM] Running Full Student Performance Analysis...")
        funcanalysis.analysis(i, i1, i2, i3)

    except Exception as e:
        print(f"\n[CRITICAL ERROR] An unexpected error occurred: {e}")
    
    finally:
        print("\n" + "="*60)
        print("   Thank you for using EduMetrics. System shutting down.")
        print("="*60)

if __name__ == "__main__":
    main()
