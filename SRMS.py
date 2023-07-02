"""

# Project: Student Record Management System

# Classes Inheritance:

                   |---> Being <---|
                   |               |
                   |               |
               Base_School       Person
                   ^               ^
                   |               |
                   |               |
                School           Student


"""

import csv, os, sqlite3, time
from abc import ABC, abstractmethod

#------ Abstraction Class/Mehtod ------#
class being(ABC):
    @abstractmethod
    def get_age(self):
        pass


class Person(being):
    def __init__(self, full_name, ID, YOB, MOB, DOB, phone_number,parents_full_names,parents_phone_numbers,parents_IDs):
#------ Encapsulation : Protected Access ------#
        self._full_name = full_name
        self._ID = ID
        self._YOB = YOB
        self._MOB = MOB
        self._DOB = DOB
        self._phone_number = phone_number
        self._parents_full_names = parents_full_names
        self._parents_phone_numbers = parents_phone_numbers
        self._parents_IDs = parents_IDs
        self._calculate_age()
    
    def _calculate_age(self):
        self._age = round(2023 - self._YOB)
    
    def get_age(self):
        return self._age

    def update_name(self,full_name):
        self._full_name = full_name
    
    def update_ID(self,ID):
        self._ID = ID
    
    def update_YOB(self,YOB):
        self._YOB = YOB
        self._calculate_age()
    
    def update_MOB(self,MOB):
        self._MOB = MOB
        self._calculate_age()
    
    def update_DOB(self,DOB):
        self._DOB = DOB
        self._calculate_age()
    
    def update_phone_number(self, phone_number):
        self._phone_number = phone_number
    
    def update_parents_names(self, parents_full_names):
        self._parents_full_names = parents_full_names
    
    def update_parents_phone_numbers(self, parents_phone_numbers):
        self._parents_phone_numbers = parents_phone_numbers
    
    def update_parents_IDs(self, parents_IDs):
        self._parents_IDs = parents_IDs

    def __str__(self):
        rep = str("""
        Name: {}
        National Number: {}
        Date Of Birth: {} / {} / {} -> {} years-old 
        Phone Number: {}
        Parents Names: {}
        Parents Phone Numbers: {}
        Parents National Numbers: {}
        """.format(self._full_name, self._ID, self._YOB,self._MOB, self._DOB, self._age,
                self._phone_number,self._parents_full_names, self._parents_phone_numbers, self._parents_IDs))
        
        return rep



class Student(Person):
    def __init__(self, student_full_name, student_ID, student_grades, student_YOB, student_MOB, student_DOB, student_class, parents_full_names, student_phone_number,
                    parents_phone_numbers, parents_IDs,**More_Information):
        
        super().__init__(student_full_name, student_ID, student_YOB, student_MOB, student_DOB, student_phone_number,parents_full_names,parents_phone_numbers,parents_IDs)

#------ Encapsulation : Protected Access ------#
        self._student_grades = student_grades
        self._student_class = student_class

        if More_Information: self._More_Information = More_Information
        else: self._More_Information = {}

#------ Method overridding ------#
    def __str__(self):
        rep = str("""
        Student Name: {}
        Student National Number: {}
        Student Grades: {}
        Student GPA: {}
        Student Date Of Birth: {} / {} / {} -> {} years-old 
        Student Class: {}
        Parents Names: {}
        Student Phone Number: {}
        Parents Phone Numbers: {}
        Parents National Numbers: {}
        """.format(self._full_name, self._ID, self._student_grades, self.Get_GPA(), self._YOB,self._MOB, self._DOB, self._age, self._student_class,
                   self._parents_full_names, self._phone_number, self._parents_phone_numbers, self._parents_IDs))
        
        if self._More_Information != {}:
            rep += "More Information:\n"
            for key,value in self._More_Information.items():
                rep  += str("              {}: {}\n".format(key, value))
            
        return rep
    
    def update_grades(self, student_grades):
        self._student_grades = student_grades
    
    def update_class(self, student_class):
        self._student_class = student_class
    
    def update_more_information(self, More_Information):
        self._More_Information = More_Information
    
    def Get_GPA(self):
        all = sum(self._student_grades)
        GPA = round(all / len(self._student_grades))
        return GPA
    
#------ Operator overriding ------#
    def __eq__(self,other):
        return (self.Get_GPA() == other.Get_GPA())
    def __gt__(self,other):
        return (self.Get_GPA() > other.Get_GPA())
    def __lt__(self,other):
        return (self.Get_GPA() < other.Get_GPA())
    def __ge__(self,other):
        return (self.__eq__(other) or self.__gt__(other))
    def __le__(self,other):
        return (self.__lt__(other) or self.__eq__(other))   



class base_school(being):
    def __init__(self, name, capacity, Foundation_year, *teachers):
#------ Encapsulation : Protected Access ------#
        self._school_name = name
        self._school_capacity = capacity
        self._teachers = teachers
        self._Foundation_year = Foundation_year
    
    def update_school_name(self,school_name):
        self._school_name = school_name
    
    def update_school_capacity(self,school_capacity):
        self._school_capacity = school_capacity

    def update_teachers(self,*teachers):
        self._teachers = teachers
    
    def print_teachers(self):
        for teacher in self._teachers:
            print(teacher)

    def get_age(self):
        return round(2023-self._Foundation_year)



class School(base_school):
    def __init__(self,name,capacity,Foundation_year,*teachers):
        
        if teachers is None:
            teachers = []
        
        super().__init__(name,capacity,Foundation_year,teachers)

#------ Encapsulation : Private Access ------#
        self.__students = []
        #self.__load_students_from_csv()
        self.__db_name = self._school_name + ".db"
        self.create_table()
        self.get_students()

    def __load_students_from_csv(self):
        filename = self._school_name + ".csv"
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                for row in reader:
                    # Create a new student object and add it to the list
                    student = Student(row[0], row[1], eval(row[2]), int(row[3]), int(row[4]), int(row[5]), row[6], row[7], row[8], eval(row[9]), eval(row[10]))
                    self.__students.append(student)
        except FileNotFoundError:
            pass
    
    def __save_students_to_csv(self):
        filename = self._school_name + ".csv"
        try:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Name", "ID", "Grades", "YOB", "MOB", "DOB", "Class", "Parents Names", "Phone Number", "Parents Phone Numbers", "Parents IDs"])
                for student in self.__students:
                    writer.writerow([student._full_name, student._ID, student._student_grades, student._YOB, student._MOB, student._DOB, student._student_class, student._parents_full_names, student._phone_number, student._parents_phone_numbers, student._parents_IDs])
        except Exception as e:
            print(f"Error occurred while saving student data to '{filename}': {str(e)}")
    
    def add_student(self, student_full_name, student_ID, student_grades, student_YOB, student_MOB, student_DOB, student_class, parents_full_names, student_phone_number,
                    parents_phone_numbers, parents_IDs,**More_Information):
        
        student = Student(student_full_name, student_ID, student_grades, student_YOB, student_MOB, student_DOB, student_class, parents_full_names, student_phone_number,
                            parents_phone_numbers, parents_IDs,**More_Information)
        
        if len(self.__students) < self._school_capacity : 
            self.__students.append(student)
        else: 
            raise Exception("School is full.")
        
        if student in self.__students:
            index = self.__students.index(student)
            #self.__save_students_to_csv()
            self.write_students(student)
            print(student,"\n Was Successfully Added to {} School At index[{}].".format(self._school_name,index))
            
    def remove_student(self, student_index):
        
        if student_index < len(self.__students):
            student = self.__students[student_index]
            self.__students.remove(student)
            self.remove_student_SQL(student._ID)
            #self.__save_students_to_csv()
            print(student,"\n Was Successfully Removed from {} School At index[{}].".format(self._school_name,student_index))
        else:
            raise Exception("Invalid Student Index.")
    
    def display_students(self,*student_indexs):
        if student_indexs:
            for student_index in student_indexs:
                print("Index : {} {}".format(student_index,self.__students[student_index]))

        else:
            student_index = 0
            for student in self.__students:
                print("Index : {} {}".format(student_index,student))
                student_index += 1
    
    def display_students_by_ID(self,*student_IDs):
        if student_IDs:
            for student_ID in student_IDs:
                student_index,student = self.student_by_ID(student_ID)
                print("Index : {} {}".format(student_index,student))
        else:
            self.display_students()
    
    def student(self,student_index):
        return self.__students[student_index]
    
    def student_by_ID(self,student_ID):
        student_index = 0
        for student in self.__students:
            if student._ID == student_ID:
                return student_index,student
            student_index += 1
    
    #------ Method overridding ------#
    def update_school_name(self,school_name):
        #os.rename(self._school_name + ".csv",school_name + ".csv")
        self._school_name = school_name
        os.rename(self.__db_name,school_name + ".db")
        self.__db_name = self._school_name + ".db"
        return 0
    
    def search_student(self,query):
        found_indexs = []

        for i in range(len(self.__students)):
            student = self.__students[i]
            if query in student.__str__():
                found_indexs.append(i)
        
        for student_index in found_indexs:
            print("Index : {} {}".format(student_index,self.__students[student_index]))
            
    
    def update_csv(self):
        self.__save_students_to_csv()

    def create_table(self):
        conn = sqlite3.connect(self.__db_name)
        cursor = conn.cursor()

        # Create a table for student records if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS students
                          (full_name TEXT, ID TEXT, student_grades TEXT,
                          YOB INTEGER, MOB INTEGER, DOB INTEGER,
                          student_class TEXT, parents_full_names TEXT,
                          phone_number TEXT, parents_phone_numbers TEXT,
                          parents_IDs TEXT)''')

        conn.commit()
        conn.close()

    def write_students(self,*students):

        # Insert a new student record into the table
        if students:
            conn = sqlite3.connect(self.__db_name)
            cursor = conn.cursor()
            for student in students:
                cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (student._full_name, str(student._ID), str(student._student_grades),
                                student._YOB, student._MOB, student._DOB, str(student._student_class),
                                str(student._parents_full_names), str(student._phone_number),
                                str(student._parents_phone_numbers), str(student._parents_IDs)))
        else:
            os.remove(self.__db_name)
            conn = sqlite3.connect(self.__db_name)
            cursor = conn.cursor()
            self.create_table()
            for student in self.__students:
                cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (student._full_name, str(student._ID), str(student._student_grades),
                            student._YOB, student._MOB, student._DOB, str(student._student_class),
                            str(student._parents_full_names), str(student._phone_number),
                            str(student._parents_phone_numbers), str(student._parents_IDs)))

        conn.commit()
        conn.close()
        return "Student record added successfully."

    def get_students(self,*indexs):
        conn = sqlite3.connect(self.__db_name)
        cursor = conn.cursor()

        # Retrieve all student records from the table
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        if indexs:
            for student_index in indexs:
                student = Student(row[0], row[1], eval(row[2]), int(row[3]), int(row[4]), int(row[5]), eval(row[6]), eval(row[7]), eval(row[8]), eval(row[9]), eval(row[10]))
                self.__students.append(student)
                print("Index : {} {}".format(student_index,student))

        else:
            student_index = 0
            for row in rows:
                #full_name, ID, student_grades, YOB, MOB, DOB, student_class, \
                #    parents_full_names, phone_number, parents_phone_numbers, parents_IDs = row

                student = Student(row[0], row[1], eval(row[2]), int(row[3]), int(row[4]), int(row[5]), eval(row[6]), eval(row[7]), eval(row[8]), eval(row[9]), eval(row[10]))
                self.__students.append(student)
                #print("Index : {} {}".format(student_index,student))
                student_index += 1

        conn.close()
    
    def remove_student_SQL(self, student_id):
        conn = sqlite3.connect(self.__db_name)
        cursor = conn.cursor()

        # Remove the student record from the table based on the ID
        cursor.execute("DELETE FROM students WHERE ID = ?", (str(student_id),))

        conn.commit()
        conn.close()
        print("Student record removed successfully.")
    
    def get_number_of_students(self):
        return len(self.__students)

def user_interface():
    os.system("clear" if os.name == "posix" else "cls")
    school = None

    print("""
                
                -----||| Student Record Management System |||-----

        


        """)
    
    name = input("Enter your School Name: ")
    capacity = int(input("\nEnter your School Capacity: "))
    foundation_year = int(input("\nEnter your School Foundation year: "))
    school = School(name, capacity, foundation_year)
    print("School created successfully!")

    #school.add_student("Mohammad",1234567890,[12,19,20,14],2001,10,23,3,
    #                 ["Hossein","Fatemeh"],9101223212,[9172321221,9392310934],[1942120323,2491394923],City="Bangalore")

    #school.add_student("Ali",1234567891,[13,12,20,12],2003,8,30,4,
    #                 ["Reza","Narges"],9101223242,[9172622212,9392710934],[1948720323,2491673923],Ciriminal_record = "Yes")

    #school.add_student("Alex",1234567892,[19,12,16,14.2],2007,2,12,1,
    #                 ["Bob","Kate"],91013133242,[9177532212,9392374234],[1948754223,2497493923])

    while True:
        os.system("clear" if os.name == "posix" else "cls")
        print("""
                
                -----||| Student Record Management System |||-----

        
        1. Add a student
        
        2. Remove a student
        
        3. Display students
        
        4. Search for a student
        
        5. Update school name

        6. Update Student Information
        
        7. Quit

        """)
        
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
                # ----- Input Validation & Error Handling ----- #

                student_full_name = input("Enter student full name : ")
                if len(student_full_name) <= 4:
                    print("** Enter a valid full name!")
                    time.sleep(1)
                    continue
                
                student_ID = int(input("Enter student ID : "))
                if len(str(student_ID)) != 10:
                    print("** Enter a valid ID!")
                    time.sleep(1)
                    continue
                
                student_grades = eval(input("Enter student grades (as a list) : "))
                for grade in student_grades:
                    if str(type(grade)) not in ["<class 'float'>","<class 'int'>"]:
                        print("** Enter valid grades!")
                        time.sleep(1)
                        continue

                student_YOB = int(input("Enter student year of birth : "))
                if len(str(student_YOB)) != 4 or student_YOB >= 2023:
                    print("** Enter a valid year of birth!")
                    time.sleep(1)
                    continue
                
                student_MOB = int(input("Enter student month of birth : "))
                if student_MOB > 12 or student_MOB < 1:
                    print("** Enter a valid month of birth!")
                    time.sleep(1)
                    continue
                
                student_DOB = int(input("Enter student day of birth : "))
                if student_DOB > 31 or student_DOB < 1:
                    print("** Enter a valid day of birth!")
                    time.sleep(1)
                    continue
                
                student_class = int(input("Enter student class : "))
                if student_class > 12 or student_class < 1:
                    print("** Enter a valid Class!")
                    time.sleep(1)
                    continue
                
                parents_full_names = eval(input("Enter parents full names (as a list) : "))
                for name in parents_full_names:
                    if str(type(name)) != "<class 'str'>" or len(name) <= 4:
                        print("** Enter valid Parents full names!")
                        time.sleep(1)
                        continue
                    
                student_phone_number = int(input("Enter student phone number : "))
                if len(str(student_phone_number)) != 10:
                    print("** Enter a valid phone number!")
                    time.sleep(1)
                    continue
                
                parents_phone_numbers = eval(input("Enter parents phone numbers (as a list) : "))
                for number in parents_phone_numbers:
                    if str(type(number)) != "<class 'int'>" or len(str(number)) != 10:
                        print("** Enter valid Parents phone numbers!")
                        time.sleep(1)
                        continue
                    
                parents_IDs = eval(input("Enter parents IDs (as a list) : "))
                for ID in parents_IDs:
                    if str(type(ID)) != "<class 'int'>" or len(str(ID)) != 10:
                        print("** Enter valid Parents IDs!")
                        time.sleep(1)
                        continue
                
                school.add_student(student_full_name, student_ID, student_grades, student_YOB, student_MOB,
                                   student_DOB, student_class, parents_full_names, student_phone_number,
                                   parents_phone_numbers, parents_IDs)            

        elif choice == "2":
                student_index = int(input("Enter student index to remove: "))
                school.remove_student(student_index)
        
        elif choice == "3":
            os.system("clear" if os.name == "posix" else "cls")
            print("""
                
                -----||| Student Record Management System |||-----

                
        1. Display All Students
        
        2. Display Specific Students
        
        3. Back to Main menu

        """)
            
            second_choice = input("Enter your choice (1-3): ")

            if second_choice == "1":
                school.display_students()
            if second_choice == "2":
                indexs = eval("["+input("Enter Student Indexs you want to display(sprate using comma): ")+"]")
                for index in indexs:
                    if str(type(index)) != "<class 'int'>" or school.get_number_of_students() <= index:
                        print("** Enter valid Student Indexs!")
                        time.sleep(1)
                        continue
                
                for index in indexs:
                    school.display_students(index)

            if second_choice == "3":
                os.system("clear" if os.name == "posix" else "cls")
                continue
        
        elif choice == "4":
                query = input("Enter search query: ")
                school.search_student(query)
            
        elif choice == "5":
                new_name = input("Enter new school name: ")
                school.update_school_name(new_name)
            
        elif choice == "6":
                os.system("clear" if os.name == "posix" else "cls")
                print("""
                
                -----||| Student Record Management System |||-----

                1. Update Student using Index

                2. Update Student using ID

                3. Back to Main menu

                """)

                second_choice = input("Enter your choice (1-3): ")
                
                if second_choice == "3":
                    os.system("clear" if os.name == "posix" else "cls")
                    continue

                if second_choice == "1":
                    os.system("clear" if os.name == "posix" else "cls")
                    print("""
                
                -----||| Student Record Management System |||-----

                """)
                    student_index = input("Enter The Student Index: ")
                    if student_index.isnumeric() == False or school.get_number_of_students() < int(student_index):
                            print("** Enter a valid Student Index!")
                            time.sleep(1)
                            continue
                
                if second_choice == "2":
                    os.system("clear" if os.name == "posix" else "cls")
                    print("""
                
                -----||| Student Record Management System |||-----

                """)
                    student_ID = input("Enter The Student ID: ")
                    if len(str(student_ID)) != 10:
                        print("** Enter a valid ID!")
                        time.sleep(1)
                        continue
                    student_index,_ =  school.student_by_ID(student_ID)
                
                os.system("clear" if os.name == "posix" else "cls")
                student_index = int(student_index)
                print("""
                
                -----||| Student Record Management System |||-----

                
        1. Update Student Full name
        
        2. Update Student ID

        3. Update Student grades

        4. Update Student Year of birth

        5. Update Student Month of birth

        6. Update Student Day of birth

        7. Update Student Class

        8. Update Parents Full Names

        9. Update Student Phone Number

        A. Update Parents Phone Numbers

        B. Update Parents IDs 
        
        C. Back to Main menu

        """)
                third_choice = input("Enter your choice (1-C): ")

                if third_choice == "1":
                    student_full_name = input("Enter student full name : ")
                    if len(student_full_name) <= 4:
                        print("** Enter a valid full name!")
                        time.sleep(1)
                        continue
                    school.student(student_index).update_name(student_full_name)
                
                if third_choice == "2":
                    student_ID = int(input("Enter student ID : "))
                    if len(str(student_ID)) != 10:
                        print("** Enter a valid ID!")
                        time.sleep(1)
                        continue
                    school.student(student_index).update_ID(student_ID)
                
                if third_choice == "3":
                    student_grades = eval(input("Enter student grades (as a list) : "))
                    for grade in student_grades:
                        if str(type(grade)) not in ["<class 'float'>","<class 'int'>"]:
                            print("** Enter valid grades!")
                            time.sleep(1)
                            continue
                    school.student(student_index).update_grades(student_grades)
                
                if third_choice == "4":
                    student_YOB = int(input("Enter student year of birth : "))
                    if len(str(student_YOB)) != 4 or student_YOB >= 2023:
                        print("** Enter a valid year of birth!")
                        time.sleep(1)
                        continue
                    school.student(student_index).update_YOB(student_YOB)
                
                if third_choice == "5":
                    student_MOB = int(input("Enter student month of birth : "))
                    if student_MOB > 12 or student_MOB < 1:
                        print("** Enter a valid month of birth!")
                        time.sleep(1)
                        continue
                    school.student(student_index).update_MOB(student_MOB)
                
                if third_choice == "6":
                    student_DOB = int(input("Enter student day of birth : "))
                    if student_DOB > 31 or student_DOB < 1:
                        print("** Enter a valid day of birth!")
                        time.sleep(1)
                        continue
                    school.student(student_index).update_DOB(student_DOB)

                if third_choice == "7":
                    student_class = int(input("Enter student class : "))
                    if student_class > 12 or student_class < 1:
                        print("** Enter a valid Class!")
                        time.sleep(1)
                        continue
                    school.student(student_index).update_class(student_class)

                if third_choice == "8":
                    parents_full_names = eval(input("Enter parents full names (as a list) : "))
                    for name in parents_full_names:
                        if str(type(name)) != "<class 'str'>" or len(name) <= 4:
                            print("** Enter valid Parents full names!")
                            time.sleep(1)
                            continue
                    school.student(student_index).update_parents_names(parents_full_names)
                
                if third_choice == "9":
                    student_phone_number = int(input("Enter student phone number : "))
                    if len(str(student_phone_number)) != 10:
                        print("** Enter a valid phone number!")
                        time.sleep(1)
                        continue
                    school.student(student_index).update_phone_number(student_phone_number)
                
                if third_choice == "A":
                    parents_phone_numbers = eval(input("Enter parents phone numbers (as a list) : "))
                    for number in parents_phone_numbers:
                        if str(type(number)) != "<class 'int'>" or len(str(number)) != 10:
                            print("** Enter valid Parents phone numbers!")
                            time.sleep(1)
                            continue
                    school.student(student_index).update_parents_phone_numbers(parents_phone_numbers)
                
                if third_choice == "B":
                    parents_IDs = eval(input("Enter parents IDs (as a list) : "))
                    for ID in parents_IDs:
                        if str(type(ID)) != "<class 'int'>" or len(str(ID)) != 10:
                            print("** Enter valid Parents IDs!")
                            time.sleep(1)
                            continue
                    school.student(student_index).update_parents_IDs(parents_IDs)
                
                if third_choice == "C":
                    os.system("clear" if os.name == "posix" else "cls")
                    continue

        elif choice == "7":
            school.write_students()
            print("\n  --- Goodbye :) --- \n")
            break
        
        else:
            print("Invalid choice. Please try again.")

        # Clear the console screen
        input()
        os.system("clear" if os.name == "posix" else "cls")

if __name__ == "__main__":
    user_interface()

#----------------------------------------------------------------
# Test Functionality of Student Record Management System

# Polymorphic Functions (Person Objects / Student Objects)
def calculate_age(somebody):
    print(somebody.get_age())
def print_object(somebody):
    print(somebody)

"""
# Create School
Vali_Asr = School("Vali Asr",100,2001,["Teacher of Class 1", "Teacher of Class 2"])

# Add Student
Vali_Asr.add_student("Mohammad",1234567890,[12,19,20,14],2001,10,23,3,
                     ["Hossein","Fatemeh"],9101223212,[9172321221,9392310934],[1942120323,2491394923],City="Bangalore")

Vali_Asr.add_student("Ali",1234567891,[13,12,20,12],2003,8,30,4,
                     ["Reza","Narges"],9101223242,[9172622212,9392710934],[1948720323,2491673923],Ciriminal_record = "Yes")

Vali_Asr.add_student("Alex",1234567892,[19,12,16,14.2],2007,2,12,1,
                     ["Bob","Kate"],91013133242,[9177532212,9392374234],[1948754223,2497493923])

# Getting Students from SQL-DB
Vali_Asr.get_students()

# Removeing the Student using ID from SQL-DB
Vali_Asr.remove_student_SQL(1234567890)

# Removeing the Student using Index
Vali_Asr.remove_student(1)

# Update the Name of the Student using Accessing the Student Object
Vali_Asr.student(0).update_name("Ali2")
Vali_Asr.student(0).update_ID(1234567890)
Vali_Asr.student(0).update_grades([19,12,16,14.2])
Vali_Asr.student(0).update_YOB(2013)
Vali_Asr.student(0).update_MOB(2)
Vali_Asr.student(0).update_DOB(21)
Vali_Asr.student(0).update_class(1)
Vali_Asr.student(0).update_parents_names(["Reza","Narges"])
Vali_Asr.student(0).update_phone_number(9101203242)
Vali_Asr.student(0).update_parents_phone_numbers([9177532292,9392374212])
Vali_Asr.student(0).update_parents_IDs([1948042223,2497401523])

# Update the Database of Students info
Vali_Asr.update_csv()

# Testing the operator overriding 
Vali_Asr.student(0) == Vali_Asr.student(0)
Vali_Asr.student(0) > Vali_Asr.student(1)
Vali_Asr.student(0) < Vali_Asr.student(1)
Vali_Asr.student(0) >= Vali_Asr.student(0)
Vali_Asr.student(0) <= Vali_Asr.student(0)

# Print the GPA of the Student
print("\n\nGPA of first student:",Vali_Asr.student(0).Get_GPA(),"\n\n")

# Print the Students of the School
Vali_Asr.display_students()

# Create person object
person1 = Person("Mohammad",1234567890,2001,10,23,["Hossein","Fatemeh"],9101223212,[9172321221,9392310934],[1942120323,2491394923])
person2 = Person("Ali",1234567891,2003,8,30,["Reza","Narges"],9101223242,[9172622212,9392710934],[1948720323,2491673923])

# Create Student object
student1 = Student("Mohammad",1234567890,[12,19,20,14],2001,10,23,3,
                     ["Hossein","Fatemeh"],9101223212,[9172321221,9392310934],[1942120323,2491394923],City="Bangalore")
student2 = Student("Ali",1234567891,[13,12,20,12],2003,8,30,4,
                     ["Reza","Narges"],9101223242,[9172622212,9392710934],[1948720323,2491673923])
 """


   