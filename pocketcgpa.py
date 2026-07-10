import os

def clear_screen():
    """Clears the terminal screen for a clean, pocket-app feel."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_grade_point(score):
    """Uses Selection Control Statements to map scores to standard 5-Point Grade Points."""
    if score >= 70:
        return 5.0, 'A'
    elif score >= 60:
        return 4.0, 'B'
    elif score >= 50:
        return 3.0, 'C'
    elif score >= 45:
        return 2.0, 'D'
    elif score >= 40:
        return 1.0, 'E'
    else:
        return 0.0, 'F'

def calculate_semester():
    """Collects course details and computes total quality points for a single semester."""
    clear_screen()
    print("=" * 45)
    print("     PPC - NEW SEMESTER CALCULATION")
    print("=" * 45)
    
    try:
        num_courses = int(input("How many courses did you take? "))
    except ValueError:
        print("\n[!] Invalid input. Numbers only.")
        input("\nPress Enter to return to main menu...")
        return 0, 0

    total_credit_units = 0
    total_quality_points = 0

    for i in range(1, num_courses + 1):
        print(f"\n--- Course {i} ---")
        try:
            units = int(input("Enter Credit Units (e.g., 2, 3, 4): "))
            score = float(input("Enter Score Obtains (0 - 100): "))
            
            # Selection control statement to validate score boundary limits
            if score < 0 or score > 100:
                print("[!] Score must be between 0 and 100. Course skipped.")
                continue
                
        except ValueError:
            print("[!] Invalid input layout. Course skipped.")
            continue

        # Fetch grading metrics
        gp, grade = get_grade_point(score)
        quality_point = units * gp
        
        total_credit_units += units
        total_quality_points += quality_point
        
        print(f"    Grade: {grade} | Grade Point: {gp} | Quality Point: {quality_point}")

    return total_quality_points, total_credit_units

def main():
    # Persistent app state variables
    cumulative_quality_points = 0.0
    cumulative_credit_units = 0
    
    while True:
        clear_screen()
        print("=" * 45)
        print("   PERSONAL POCKET CGPA CALCULATOR (PPC)")
        print("=" * 45)
        print(" [1] Add New Semester Data")
        print(" [2] View Current Pocket CGPA Status")
        print(" [3] Reset All Pocket Logs")
        print(" [4] OFF (Close Calculator)")
        print("=" * 45)
        
        choice = input("Select an option (1-4): ").strip()
        
        # Selection Control Statements processing the core application logic
        if choice == '1':
            qp, units = calculate_semester()
            
            # Validation control check
            if units > 0:
                semester_gpa = qp / units
                print("\n" + "-" * 45)
                print(f" Semester GPA: {semester_gpa:.2f}")
                print("-" * 45)
                
                # Accumulate history parameters for total CGPA tracking
                cumulative_quality_points += qp
                cumulative_credit_units += units
            else:
                print("\n[!] No valid data recorded for this semester.")
            
            input("\nPress Enter to return to main menu...")

        elif choice == '2':
            clear_screen()
            print("=" * 45)
            print("         CURRENT CGPA POCKET STATUS")
            print("=" * 45)
            print(f" Total Registered Units : {cumulative_credit_units}")
            print(f" Total Quality Points   : {cumulative_quality_points:.2f}")
            
            # Selection control ensuring safe math boundaries avoiding division by zero
            if cumulative_credit_units > 0:
                current_cgpa = cumulative_quality_points / cumulative_credit_units
                print(f" Current Standing CGPA  : {current_cgpa:.2f}")
                print("-" * 45)
                
                # Dynamic advice statements based on current CGPA scale bounds
                if current_cgpa >= 4.50:
                    print(" Class: First Class Honours 🌟")
                    print(" Advice: Maintain the momentum, you are flying high!")
                elif current_cgpa >= 3.50:
                    print(" Class: Second Class Honours (Upper Division) 🚀")
                    print(" Advice: Push a bit harder to touch the stars!")
                elif current_cgpa >= 2.40:
                    print(" Class: Second Class Honours (Lower Division) 👍")
                    print(" Advice: Review your study targets to scale higher.")
                elif current_cgpa >= 1.50:
                    print(" Class: Third Class Honours")
                    print(" Advice: Significant focus and tutorial support recommended.")
                else:
                    print(" Class: Pass / Probation Warning ⚠️")
                    print(" Advice: Immediate intervention needed. See your adviser.")
            else:
                print(" Current Standing CGPA  : 0.00")
                print("-" * 45)
                print(" [!] No semester data added yet. Select option [1] to begin.")
                
            print("=" * 45)
            input("\nPress Enter to return to main menu...")

        elif choice == '3':
            confirm = input("\nAre you sure you want to clear your data records? (y/n): ").lower()
            if confirm == 'y':
                cumulative_quality_points = 0.0
                cumulative_credit_units = 0
                print("\n[✓] Pocket database reset successful.")
            else:
                print("\n[x] Reset operation cancelled.")
            input("\nPress Enter to continue...")

        elif choice == '4' or choice.upper() == 'OFF':
            print("\nShutting down PPC... Goodbye!")
            break

        else:
            print("\n[!] Invalid Option! Please choose a number from 1 to 4.")
            input("\nPress Enter to try again...")

if __name__ == "__main__":
    main()
