

# Importing all your modules
import funcsem       # File 4: The Data Entry & Average Logic
import funchighpsem     # File 2: Semester-wise Toppers
import funchighpsub     # File 3: Subject-wise Highest Marks
import funcanalysis    # File 1: Full Student Performance Analysis
import funchighsub4sem # File 5: Overall Subject Toppers (4 Semesters)

def main():
    # HEADER
    while True:
        print("="*60)
        print("       WELCOME TO THE EDUMETRICS CONTROL CENTER")
        print("="*60)

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
 

        # STEP 2.5: OVERALL SUBJECT TOPPERS (File 5)
        print("\n[SYSTEM] Calculating Overall Subject Toppers (Sem 1-4)...")
        funchighsub4sem.show_overall_subject_toppers(i, i1, i2, i3)
        
        
        # STEP 3: SUBJECT-WISE HIGHEST MARKS (File 3)
        print("="*60)
        print("       TOPPERS IN EACH SUBJECT")
        print("="*60)
        print("\n[SYSTEM] Calculating Subject-wise Highest Marks...")
        funchighpsub.find_highest_per_subject(i, i1, i2, i3)
        # STEP 4: FULL STUDENT PERFORMANCE ANALYSIS (File 1)
        print("\n[SYSTEM] Running Full Student Performance Analysis...")
        funcanalysis.analysis(i, i1, i2, i3)

        print("\n" + "="*60)
        ans = input("Do you want to use EduMetrics again? (y/n): ").lower()
        if ans == 'y':
            print("\n" + "-"*30)
            print("Restarting for a new session...")
            print("-"*30)
            # The loop goes back to the top of 'while True'
            continue 
        else:
            print("\n" + "="*60)
            print("   Thank you for using EduMetrics. System shutting down.")
            print("="*60)
            # This breaks the loop and closes the program
            break 

if __name__ == "__main__":
    main()
    
