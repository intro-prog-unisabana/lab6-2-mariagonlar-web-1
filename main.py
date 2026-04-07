from grades_manager import add_student, avg_by_student
def main():
    print("Welcome to the Student Grades Manager!\n")
    grades = {}
    while True:
        print("Select an option:")
        print("1. Add a student")
        print("2. Print student grade averages")
        print("3. Exit")
        choice = input()
        if choice == "1":
            grades = add_student(grades)
        elif choice == "2":
            print("Select an option:")
            print("a. Display all students")
            print("b. Display selected students")
            sub_choice = input()
            if sub_choice == "a":
                avg_by_student(grades)
            elif sub_choice == "b":
                names = input("Enter student names (comma-separated):\n")
                name_list = names.split(",")
                avg_by_student(grades, name_list)
            else:
                print("Invalid option selected!")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option selected!")


if __name__ == "__main__":
    main()