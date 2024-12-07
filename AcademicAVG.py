def avg():
    coursee = []
    grades_sum = 0
    total_credits = 0

    try:
        num_courses = int(input('Enter number of courses: '))
        if num_courses <= 0:
            raise ValueError("It must be a valid number.")

        for i in range(num_courses):
            course_name = input(f'{i + 1}) Enter course name: ')
            if course_name.isnumeric():
                raise ValueError("Course name must to be a string.")

            # Save the academic credits per each course
            academic_credits = int(input(f'Enter the credit points for {course_name}: '))
            if academic_credits < 0:
                raise ValueError("Credit points must be positive.")
            elif academic_credits == 0:
                raise ValueError("Credit points cant be 0.")

            # Save The Grade
            grade = int(input(f'Enter the grade for {course_name}: '))
            if grade < 0 or grade > 100:
                raise ValueError("Grade must be between 0 and 100.")

            # Save The Course
            courses.append((course_name, academic_credits, grade))
            grades_sum += academic_credits * grade
            total_credits += academic_credits
            print()

        # Calculate The Average
        average = grades_sum / total_credits
        print(f"The Average is: {average:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


avg()
