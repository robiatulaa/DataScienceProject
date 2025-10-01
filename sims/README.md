# Sudent Information Management System
## Group Project
### Monash University, Indonesia

### Group Members:
- Reza Maliki Akbar
- Hugo Andrew Prathama
- Robiatul Adawiyah Al-Qosh

### Project Description
This project is aimed at developing competencies in designing, constructing, testing, and documenting a Python program based on specified programming standards. It contributes to the learning outcomes of restructuring computational programs into manageable modules, demonstrating I/O strategies, and applying testing and exception handling techniques.

The task involves developing a student information management system that will allow different users (Admin, Teacher, Student) to interact with the system according to their roles and permissions. The system utilizes two files, `user.txt` and `unit.txt`, to manage data related to users and academic units, respectively.


### File Structure and Descriptions

#### `main.py`
Main application entry point. Initializes the application and provides the main menu for user interaction.

#### `classes/unit.py`
Defines the Unit class with attributes and methods to represent and manage academic units.

#### `classes/user.py`
Defines the base User class, which is extended by specific user types such as students, teachers, and administrators.

#### `classes/user_admin.py`
Extends the User class to define UserAdmin, containing functionalities specific to an administrator's role.

#### `classes/user_student.py`
Extends the User class to define UserStudent, containing functionalities specific to a student's role.

#### `classes/user_teacher.py`
Extends the User class to define UserTeacher, containing functionalities specific to a teacher's role.

#### `config.py`
Contains configuration variables and constants used throughout the application.

#### `file_readwrite.py`
Provides functions for reading from and writing to data files used by the application.

### Directories
- `data`: Contains data files such as `unit.txt` and `user.txt` that store information about units and users, respectively.
- `score_charts`: Stores generated images of students score distribution charts for various units.
- `docs`: Contains documentation files such as user manual `userManual_group9.pdf`, group diary `Group09_Diary.pdf`, and test strategies document `Group09_TestStrategies.pdf`.
- `tests`: Scripts for running tests of the program (not included in submission file). Just want to check and test using `unittest`. 

### Setup and Execution
Detailed instructions on how to set up and run the project will be included in the user manual [`docs/userManual_group9.pdf`](docs/userManual_group9.pdf). This manual will guide the user through the initial setup, main features, and operational procedures of the student information management system.

### Test Strategy
Our test strategy ensures application robustness and reliability. It aims to verify functionality, meet requirements, and resolve defects. We did it manually and automatically. For detailed test cases and methodologies, refer to [`docs/Group09_TestSrategies.pdf`](docs/Group09_TestSrategies.pdf). 

### Contributions
The three of us were working hardly to build this application 😁💪

### Group Diary
Our project includes a "Group Diary" detailing our team's progress and experiences while developing the Student Information Management System for ITI9136 Assignment 3. It offers insights into our collaboration, challenges, and logs of our meeting.
Although, we have also a WhatsApp channel group to maintain our communication on regular basis.

Located on: [`docs/Group09_Diary.pdf`](docs/Group09_Diary.pdf)

### References
[1] https://python.plainenglish.io/modularization-on-python-68b7dd6982cf


[2] https://realpython.com/pytest-python-testing/


[3] https://www.geeksforgeeks.org/class-method-vs-static-method-python/


[4] https://www.datacamp.com/tutorial/matplotlib-tutorial-python


[6] https://stackoverflow.com/questions/1977362/how-to-create-module-wide-variables-in-python


[7] https://grzegorz-makowski.medium.com/understanding-self-and-cls-in-python-b674f5e5951d


[8] https://www.pythonpool.com/python-cls-vs-self/


[9] https://www.dataquest.io/blog/regex-cheatsheet/ 


[10] https://manytools.org/hacker-tools/convert-images-to-ascii-art/ 


[11] https://docs.python.org/3/library/exceptions.html 


[12] https://pymbook.readthedocs.io/en/latest/pep8.html 


[13] https://easypythondocs.com/validation.html 


[14] https://www.w3docs.com/snippets/python/what-is-init-py-for.html 


[15] https://stackoverflow.com/questions/2673651/inheritance-from-str-or-int 


[16] https://www.greenteapress.com/thinkpython/html/book018.html 


[17] https://realpython.com/inheritance-composition-python/ 

[18] https://docs.python-guide.org/writing/structure/

[19] https://dagster.io/blog/python-project-best-practices


[20] B. Miller and D. Ranum, "Problem Solving with Algorithms and Data Structures Using Python," Wilsonville, OR, Franklin, Beedle & Associates Inc., 2011. 


[21] B. R. Preiss, Data Structures and Algorithms with Object-Oriented Design Patterns in Python, 2003.

[22] M. Lutz, Programming Python. O'Reilly Media, 2010.


---

