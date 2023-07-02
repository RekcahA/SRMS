
# Student Record Management System

## Project Description

The Student Record Management System is a Python program designed to manage student records in a school. 
    It provides functionality for adding students, updating their information, and displaying student details.
        The program utilizes object-oriented programming principles such as encapsulation, inheritance, and polymorphism to achieve its functionality.

---> the code provided is a basic implementation and can be further enhanced and extended based on specific requirements and use cases.

## Code Overview

The project consists of several classes:

1. `being` (Abstract Class): 
        An abstract class that defines the basic structure for a being.

2. `Person` (Inherits from `being`):
        Represents a person and includes attributes such as 
            full name, ID, date of birth, phone number, and parents' information.
                It also calculates the age based on the year of birth.

3. `Student` (Inherits from `Person`):
        Represents a student and extends the `Person` class.
            It includes additional attributes such as student grades, student class, and more information.
                It provides methods to update grades, class, and additional information.
                    It also calculates the GPA (Grade Point Average) based on the student's grades.
                        The class overrides the string representation method and implements operator overloading for comparison.
                            It also save and load Students records using CSV (Comma separated values) files.

3. `base_school` (Inherits from `being`): 
        An abstract base class that represents a school, with attributes such as school name, capacity, and teachers.
            It inherits from being and provides methods for updating school-related information.

4. `School` (Inherits from `base_school`):
        A class that represents a specific school, inheriting from base_school.
            It adds functionality for managing students, including adding, removing, displaying, and searching for students.
                It also uses SQLite to store student records in a database.

## Functionality

The code includes the following functionality:

1. Creating a school object:
    
    Vali_Asr = School("Vali Asr", 10)
    

2. Adding students to the school:
    
    Vali_Asr.add_student(...)
    

3. Removing students from the school:
    
    Vali_Asr.remove_student(student_index)
    

4. Updating student information:

    Vali_Asr.student(student_index).update_name(full_name)
    Vali_Asr.student(student_index).update_grades(grades)
    Vali_Asr.student(student_index).update_class(student_class)
    
    

5. Displaying student details:
    
    Vali_Asr.display_students()
    

6. Calculating GPA:
    
    Vali_Asr.student(student_index).Get_GPA()
    

7. Polymorphic functions:
    - Calculating age:
        
        calculate_age(somebody)
        
    - Printing object details:
        
        print_object(somebody)
        

*** The Student Record Management System provides a flexible and organized approach to manage student records within a school.
        It allows for easy addition, removal, and updating of student information.
            The code demonstrates the use of object-oriented programming principles to create a robust and efficient system for managing student records.
