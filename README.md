# Student Record Management System

This is a Python project that implements a Student Record Management System. The system allows you to manage student records, including their personal information, grades, and more. The project uses classes and inheritance to create a robust and flexible system.

## Project Structure

The project consists of the following classes and inheritance hierarchy:

```
    |-----Being-----|
    |               |
Base_School       Person
    ^               ^
    |               |
 School           Student
```

- `Being` is an abstract base class (ABC) that defines an abstract method `get_age()`.
- `Person` is a concrete class that inherits from `Being` and represents a general person. It contains attributes and methods related to a person's personal information, such as full name, ID, date of birth, and phone number.
- `Student` is a subclass of `Person` and represents a student. It adds additional attributes and methods specific to a student, such as grades, GPA, and class. It also overrides some methods from the `Person` class.
- `Base_School` is another concrete class that inherits from `Being` and represents a base school. It contains attributes and methods related to a school, such as school name, capacity, and teachers.
- `School` is a subclass of `Base_School` and represents a specific school. It adds additional attributes and methods specific to a school, such as a list of students. It also overrides some methods from the `Base_School` class.

## Features

The Student Record Management System provides the following features:

- Add a new student to the system, including their personal information, grades, and more.
- Remove a student from the system based on their index.
- Display student records, either all students or specific students based on their index or ID.
- Search for a specific student record based on a query.
- Update the school name and capacity.
- Update a student's information, such as grades, class, and more.
- Calculate and display a student's GPA.
- Compare students based on their GPA using comparison operators (e.g., `==`, `>`, `<`).

## Getting Started

To run the Student Record Management System, follow these steps:

1. Clone the repository to your local machine.
2. Make sure you have Python installed (version 3.6 or above).
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the command `python main.py` to start the program.

## Usage

The program will provide you with a command-line interface to interact with the Student Record Management System. You can use the available commands to perform various operations on student records.

Here are some example commands you can use:

- `add`: Add a new student to the system.
- `remove`: Remove a student from the system.
- `display`: Display student records.
- `search`: Search for a student record based on a query.
- `update`: Update a student's information.
- `compare`: Compare two students based on their GPA.

Please refer to the program's documentation or source code for more details on available commands and their usage.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for more information.

---

This README provides an overview of the Student Record Management System project. For more details, please refer to the source code.

Happy coding!

"""
