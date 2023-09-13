
#########    STUDENT MANAGEMENT SYSTEM      #########

# our list students where we are adding the details
students = []

# a Student class with attributes name,roll_number,grade,marks
class Student :
    def __init__(self, name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks= marks
        self.grade = self.calculateGrade()

    # methods to set the name, roll_number,grade,marks attributes
    def setName(self,name):
        self.name = name

    def setRoll_number(self,roll_number):
        self.roll_number = roll_number

    def setGrade(self,grade):
        self.grade = grade

    def setMarks(self,marks):
        self.marks = marks
        self.grade = self.calculateGrade()
        return self.marks

    # methods to return the name, roll_number,grade,marks attributes
    def getName(self):
        return self.name

    def getRoll_number(self):
        return self.roll_number

    def getGrade(self):
        return self.grade

    def getMarks(self):
        return self.marks

    # calculating the grade based on the marks obtained.
    # i am going to use the makerere grading system
    # https://new.mak.ac.ug/web/students/grading
    def calculateGrade(self):
        if (0 <= self.marks and 39 >= self.marks ):
            return "F"
        elif (40<= self.marks and  49>= self.marks ):
            return "E"
        elif (50<= self.marks and  59>= self.marks ):
            return "D"
        elif (60<= self.marks and  69>= self.marks):
            return "C"
        elif (70<= self.marks and  79>= self.marks):
            return "B"
        elif (80<= self.marks and  100>= self.marks):
            return "A"
        else :
            print("\nINVALID ENTRY!! \n\n")

# function that allows users to add new students to the student system.
def adding_students():
    name = input("Please enter the student's name: ")
    roll_number = input("Please enter the student's roll number: ")
    marks = int(input("Please enter the student's marks: " ))
    student = Student(name,roll_number,marks)
    students.append(student)
    print("\nThe details of the student have been added successfully.\n\n")
    

# a function to display information of a specific student.
def display_student_info():
    if not students :
        print('\nNo records found!\n')
        return
    roll_number =input("Enter the student's roll number to display their information: ")
    for student in students:
        if student.getRoll_number() == roll_number:
            print("\n_______Student's information._______\n")
            print("NAME;",student.getName().title())
            print("ROLL NUMBER;",student.getRoll_number())
            print("GRADE;",student.getGrade())
            print("MARKS;",student.getMarks())
            print("___________________________________________________\n\n")
            break
        else:
            print("\nThe roll number does not match any student in the system.\n\n")

# a function to update the information of a specific student
# it allows them to update any attribute of the student (name, roll number,grade or mark)
def update_student_info():
    if not students :
        print('\nThere are no existing Records!.\n')
        return
    roll_number = input("\nEnter the student's roll number: ")
    
    for student in students:
        if student.getRoll_number()==roll_number:
            print("\n\nChoose the number corresponding to your choice (1-3).\n")
            print("1.Update the student's name.\n")
            print("2.Update the student's roll number.\n")
            print("3.Update the student's marks.\n\n")
            
            option=input("Enter your choice:")
            if option == '1':
                new_name=input("Enter the student's new name :")
                student.setName(new_name)
                print("\nThe Student's Name has been Updated.\n")
            elif option == '2':
                new_roll_no=input("Enter the student's new roll number :")
                student.setRoll_number(new_roll_no)
                print("\nThe Student's Roll number has been Updated.\n")
            elif option == '3':
                new_marks=int(input("Enter the student's new Marks: "))
                student.setMarks(new_marks)
                print("\nThe Student's Marks has been updated.\n")
            else :
                 print("\nInvalid Option! \nTRY AGAIN\n")
    return
    print("\nStudent does not exist in the system.\n\n")

# A function to delete a student from the system.
# the user enters a roll number to remove the corresponding student
def del_student():
    if not students :
        print ("There are no records present!!")
        return
    roll_number = input("Enter the student's roll number to be deleted:")
    for student in students:
        if student.getRoll_number() == roll_number:
            students.remove(student)
            print(roll_number ," has been successfully deleted from the system.\n")
            return
        else:
            print("\nStudent does not exist in the system.\n")

# function to display information for our user to select
def menu():
    print('\n#########    STUDENT MANAGEMENT SYSTEM      #########\n')
    print("************** MAIN MENU *******************")
    print("1. Add Student                             *")
    print("2. Display Student Information             *")
    print("3. Update Student Details                  *")
    print("4. Delete Student from system              *")
    print("5. Quit !!                                 *")
    print("********************************************")

while True:
    menu()
    option = input("\nPlease select an option(1-5) from the Menu:")
    
    if option =='1':
        adding_students()
    elif option =='2':
        display_student_info()
    elif option =='3':
        update_student_info()
    elif option =='4':
        del_student()
    elif option =='5':
        option2=input("Are you sure ...?(y/n): ")
        if option2 =="y":
            print("Exiting>>>>...")
            print("THE END")
            break
    else:
        print("Invalid Choice.!!\n Please try again.")
        



# BEIJUKA BRUNO
# student_manage.property assignment
# abdunoor.kalibala@netlabsug.org.
# Thank you
        
