def loadDatabase():
    '''
        This function reads data from a file and loads it into a list.
        If no file with the specified name exists, it creates a new one and continues.
    '''
    global students
    try:
        with open("Database.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()  # Remove any leading/trailing whitespace
                if not line:  # Skip empty lines
                    continue
                info = line.split(",")
                if (len(info) != 3):  # Check if line has exactly 3 parts (id, name, dept)
                    with open("error_log.txt", "a") as error:
                        error.write(f"Invalid line: {line}\n")  # Log the invalid line
                    continue
                student = {'id': info[0], 'name': info[1], 'dept': info[2]}
                students.append(student)
    except FileNotFoundError:
        with open("Database.txt", "w") as file:
            pass
            
def updateDatabase():
    '''
        This function updates the database file whenever any changes are made.
    '''
    with open("Database.txt", "w") as file:
        for student in students:
            file.write(f"{student['id']},{student['name']},{student['dept']}\n")

def Main():
    '''
        This is the main function which takes commands from the user and executes them by calling the appropriate functions.
    '''
    print("Welcome to the Student Information System (SIS). Please choose an option from the menu below.")
    while (True):
        print("\nMain menu:\n──────────\n1. Add a New Student\n2. View All Students\n3. Search for a Student\n4. Edit a Student Profile\n5. Delete a Student Profile\n6. Exit")
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            addStudent()
        elif choice == "2":
            viewStudent()
        elif choice == "3":
            searchStudent()
        elif choice == "4":
            editStudent()
        elif choice == "5":
            deleteStudent()
        elif choice == "6":
            print("\nThank you for using the system. Have a great day!")
            break
        else:
            print("\nInvalid choice. Please input a valid option.\n")

def addStudent():
    '''
        To add a student, I created three infinite loops with some if-elif conditions to take input for the student’s ID, name, and department.
        The conditions ensure the inputs meet specific criteria; otherwise, the loop keeps asking for the correct input.
        Once all criteria are met, the loop breaks, and the inputs are added as a dictionary to a list and saved to the database file.
    '''
    print("\nPlease enter a new Student ID. Ensure the ID is within 20 characters and does not contain spaces or special characters. Type 'X' to cancel.")
    while (True):
        id = input("Student ID : ").strip() # Input with strip function for removing extra space
        if (id == "X"):
            return
        elif not id:
            print("\nThe ID field can't be empty. Please try again.")
            continue
        elif (len(id) > 20):
            print("\nThe ID field can't exceed 20 characters. Please try again.")
            continue
        elif (id.isalnum() == False):
            print("\nThe ID must not contain space or special charecters. Please try again.")
            continue
        for student in students:
            if (student['id'] == id):
                print("A Student with the same ID already exists.")
                return
        break
    print("\nPlease enter the student's name. The name must be between 3 to 50 characters. Type 'X' to cancel.")
    while (True):
        name = input("Student Name : ").strip()
        if (name == "X"):
            return
        elif not name:
            print("The name field can't be empty. Please try again.")
            continue
        elif ((len(name)<3) or (len(name) > 50)):
            print("The name must be between 3 to 50 characters. Please try again.")
            continue
        elif not all(char.isalpha() or char.isspace() or char =="." for char in name):
            print("The name can only contain alphabatical charecters and dot. Please try again.")
            continue
        '''
            Capitalize the first letter of each word without touching other letters, also remove extra space.
        '''
        name = ' '.join(word[0].upper() + word[1:] for word in name.split() if word)
        break
    print("\nPlease enter the department name. The name must not exceed 50 characters. Type 'X' to cancel.")
    while (True):
        dept = input("Department Name : ").strip()
        if (dept == "X"):
            return
        elif not dept:
            print("Field can't be empty. Please try again.")
            continue
        elif ((len(name)<3) or (len(dept) > 50)):
            print("Department name must be between 3 to 50 characters. Please try again.")
            continue
        elif not all(char.isalpha() or char.isspace() or char =="." or char =="&" for char in dept):
            print("The department name can only contain alphabatical charecters, dot and aparend sign. Please try again.")
            continue
        dept = ' '.join(word[0].upper() + word[1:] for word in dept.split() if word)
        break
    students.append({'id': id, 'name': name, 'dept': dept})
    updateDatabase()
    print("\nStudent information has been added successfully.\n")

def viewStudent():
    '''
        To display all student information, I created a table using functions like max(), ljust(), and center().
        The purpose of the table is to make look good and organized while also fitting more student information on the screen.
        I also sorted the information by student ID to make it easier to find and looks organized.
    '''
    if (len(students) == 0):
        print("\nNo student information available.\n")
        return
    temp = sorted(students, key = lambda x:x["id"]) #Sorting by Student ID
    a, b, c=[10], [12], [15]
    d="Total student: "+str(len(temp)).rjust(2,'0')
    for i in students:
        a.append(len(i["id"]))
        b.append(len(i["name"]))
        c.append(len(i["dept"]))
    print("┌─" + "─" * max(a) + "─┬─" + "─" * max(b) + "─┬─" + "─" * max(c) + "─┐")
    print("│ " + "Student ID".center(max(a)) + " │ " + "Student Name".center(max(b)) + " │ " + "Department Name".center(max(c)) + " │")
    print("├─" + "─" * max(a) + "─┼─" + "─" * max(b) + "─┼─" + "─" * max(c) + "─┤")
    for student in temp:
        print("│ " + student["id"].center(max(a)) + " │ " + student["name"].ljust(max(b)) + " │ " + student["dept"].ljust(max(c)) + " │")
    print("├─" + "─" * max(a) + "─┴─" + "─" * max(b) + "─┴─" + "─" * max(c) + "─┤")
    print("│ " + d.ljust(max(a)+max(b)+max(c)+6)+" │")
    print("└─" + "─" * max(a) + "───" + "─" * max(b) + "───" + "─" * max(c) + "─┘\n")
    
def searchStudent():
    '''
        In the search function, it is possible to search not only by student ID but also by name or department.
        For name and department searches, partial matching is supported but a minimum of 3 characters is required.
        I also added option to display all matching student information as the search result.
    '''
    search = input("\nEnter your queary to search: ").strip()
    temp = []
    n=1
    if len(search)<3:
        for student in students:
            if (search == student["id"]):
                temp.append({'id': student["id"], 'name': student["name"], 'dept': student["dept"]})
    else:
        for student in students:
            if (search == student["id"]) or (search.lower() in student["name"].lower()) or (search.lower() in student["dept"].lower()):
                temp.append({'id': student["id"], 'name': student["name"], 'dept': student["dept"]})
    if not temp:
        print(f"\nNo match found for \"{search}\".\n\nTIPS:\n01. You can search by student ID as well as name or department.\n02. Searching with student ID requires full ID number.\n03. In case name or dept , you have to input atleast 3 letter.")
    else:
        if len(temp)==1:
            print("\n1 match found for \""+search+"\".\n"+"─"*(21+len(search)))
        else:
            print("\n"+str(len(temp))+" match's found for \""+search+"\".\n"+"─"*(len(temp)+21+len(search)))
        for i in temp:
            if len(temp)>1:
                print(n,"\n─"+"─"*len(str(n)))
            print("Student ID      :", i["id"])
            print("Student Name    :", i["name"])
            print("Department Name :", i["dept"], "\n")
            n+=1
    return
    
def editStudent():
    '''
    In the edit function, it is possible to update specific details like student ID, name, or department by selecting the desired option from a menu.
    Similar to the add student function, each input is continuously validated until it meets the required criteria.
    '''
    id = input("\nEnter a valid student ID number: ").strip()
    for student in students:
        if student["id"] == id:
            print("\nWhat do you want to edit?\n1. ID number\n2. Name\n3. Department\n")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                while (True):
                    new_id = input("Enter correct student ID : ").strip()
                    if (new_id == "X"):
                        return
                    elif not new_id:
                        print("\nThe ID field can't be empty. Please try again.")
                        continue
                    elif (len(new_id) >= 20):
                        print("\nThe ID field can't exceed 20 characters. Please try again.")
                        continue
                    elif (new_id.isalnum() == False):
                        print("\nThe ID must not contain space or special charecters. Please try again.")
                        continue
                    for student in students:
                        if (student['id'] == new_id):
                            print("A Student with the same ID already exists.")
                            return
                    break
                student["id"] = new_id
                updateDatabase()
                print("\nStudent information updated successfully!\n")
            elif choice == "2":
                while (True):
                    new_name = input("Enter correct name : ").strip()
                    if (new_name == "X"):
                        return
                    elif not new_name:
                        print("The name field can't be empty. Please try again.")
                        continue
                    elif ((len(new_name)<3) or (len(new_name) > 50)):
                        print("The name must be between 3 to 50 characters. Please try again.")
                        continue
                    elif not all(char.isalpha() or char.isspace() or char =="." for char in new_name):
                        print("The name can only contain alphabatical charecters and dot. Please try again.")
                        continue
                    new_name = ' '.join(word[0].upper() + word[1:] for word in new_name.split() if word)
                    break
                student["name"] = new_name
                updateDatabase()
                print("\nStudent information updated successfully!\n")
            elif choice == "3":
                while (True):
                    new_dept = input("Enter correct department name : ").strip()
                    if (new_dept == "X"):
                        return
                    elif not new_dept:
                        print("Field can't be empty. Please try again.")
                        continue
                    elif ((len(new_dept)<3) or (len(new_dept) > 50)):
                        print("Department name must be between 3 to 50 characters. Please try again.")
                        continue
                    elif not all(char.isalpha() or char.isspace() or char =="." or char =="&" for char in new_dept):
                        print("The department name can only contain alphabatical charecters, dot and aparend sign. Please try again.")
                        continue
                    new_dept = ' '.join(word[0].upper() + word[1:] for word in new_dept.split() if word)
                    break
                student["dept"] = new_dept
                updateDatabase()
                print("\nStudent information updated successfully!\n")
            else:
                print("\nInvalid choice. Please try again.\n")
            return
    print(f"\nNo student found with the ID: {id}.\n")
    return

def deleteStudent():
    '''
        In the delete function, it is possible to remove a single student or multiple students by entering their ID numbers, separated by commas.
        Additionally, it is posaible to delete the entire database by typing "ALL".
    '''
    print(r'To delete a student profile please enter the student ID(s). To delete multiple, type desired student IDs one after another followed by a comma(,). Type "ALL" to delete the whole database. Type "X" to cancel.')
    while(True):
        ids = input("\nEnter Student Id: ").strip()
        del_list = ids.split(",")
        deleted, other=[], []
        if not ids:
            print("\nYou have to input atleast one student ID.")
            continue
        elif ids == "X":
            return 
        elif ("ALL" in del_list):
            confirm = input("\nAre you sure you want to delete all student profiles? (yes/no): ").strip().lower()
            if confirm == "yes":
                students.clear()
                print("\nAll student profiles deleted successfully.")
                updateDatabase()
                return
            print("\nDeletion process cancelled.")
            return
        for i in del_list:
            found = False
            for student in students:
                if (student["id"] == i.strip()):
                    students.remove(student)
                    deleted.append(i.strip())
                    found = True
                    break
            if not found:
                other.append(i.strip())
        if (len(deleted)==1):
            print(f"\nStudent with ID number \"{deleted[0]}\" deleted successfully.\n")
        if (len(deleted)>1):
            print("\nStudent with ID number \""+'","'.join(deleted[:-1])+"\" and \""+deleted[-1]+"\" deleted successfully.\n")
        if (len(other)==1):
            print(f"\nNo student found with the ID number \"{other[0]}\".\n")
        if (len(other)>1):
            print("\nNo student found with the ID number \""+ '","'.join(other[:-1])+"\" and \""+other[-1]+"\".\n")
        updateDatabase()
        break
        return
students = [] 
loadDatabase()
Main()
