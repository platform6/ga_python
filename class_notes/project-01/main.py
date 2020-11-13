data = {
    10001:
        {
            'first_name': 'Chris',
            'last_name': 'Herzog',
            'email': 'chriher22@aol.com',
            'classes_taken': ('CSC126', 'CSC211', 'CSC326'),
            'grades_received': ('A', 'C', 'F'),
            'type': 'student'
        },
    10002:
        {
            'first_name': 'Joseph',
            'last_name': 'Smith',
            'email': 'JosephSSmith@rhyta.com',
            'classes_taken': ('CSC456', 'CSC121', 'ENG151'),
            'grades_received': ('A', 'C', 'A'),
            'type': 'student'
        },
    10003:
        {
            'first_name': 'Kelli',
            'last_name': 'Marshall',
            'email': 'JosephSSmith@rhyta.com',
            'classes_taken': ('CSC456', 'CSC121', 'ENG120', 'ENG121', 'ENG151', 'ENG230'),
            'grades_received': ('A', 'A', 'A', 'A', 'A', 'A'),
            'type': 'student'
        },
    10004:
        {
            'first_name': 'Manuel',
            'last_name': 'Horn',
            'email': 'ManuelCHorn@dayrep.com',
            'classes_taken': ('CSC456', 'CSC121'),
            'grades_received': ('A', 'C'),
            'type': 'student'
        },
    10005:
        {
            'first_name': 'Kevin',
            'last_name': 'Lacour',
            'email': 'KevinBLacour@teleworm.us',
            'classes_taken': ('CSC211', 'CSC220'),
            'grades_received': ('F', 'F'),
            'type': 'student'
        },
    10006:
        {
            'first_name': 'Suresh',
            'last_name': 'Sigera',
            'email': 'sureshsigera@ms.edu',
            'password': 'J&hqweh12e7d2n281',
            'type': 'staff'
        },
    10007:
        {
            'first_name': 'Ann',
            'last_name': 'Chatman',
            'email': 'AnnBChatman@ms.edu',
            'password': 'J&hqweh12e7d2n28qq1',
            'type': 'staff'
        },
}


def admin_login():
    """
    validate administrator (staff) login credentials
    if the login is successful, show the menu with following functionality:
    add_new_student, list_all_students, search_students, remove_student and display_single_record
    """
    login = True
    login_attempts = 0
    profile_dict = {}


    print("""
          -------------LOG IN---------------

          """)


    while login:
        acct_id = int(input("Account ID:  "))
        if acct_id in get_staff_id_list():
            print(f'---- {acct_id} found  ----- ')
            profile_dict = (data.get(acct_id, None))
            break
        else:
            print(f'Account not found by account id {acct_id}. Please reenter.')
            login_attempts += 1
            if login_attempts > 2:
                print("Login attempts exceeded - exiting program")
                login = False


    if login != False:
        profile_email = profile_dict.get('email', None)
        profile_password = profile_dict.get('password', None)


        input_email = input("Email:  ")
        input_password = input("Password:  ")

        if profile_email == input_email and profile_password == input_password:
            print(f"Hello, {profile_dict.get('first_name')} -- redirecting to main menu")
            menu()
        else:
            print("You are not an admin - exiting program")

def get_staff_id_list():
    staff_id = []
    for x, y in enumerate(data):
        staff_dict = data.get(y)
        if staff_dict.get('type') == 'staff':
            staff_id.append(y)
    return staff_id

def get_student_id_list():
    student_id = []
    for x, y in enumerate(data):
        student_dict = data.get(y)
        if student_dict.get('type') == 'student':
            student_id.append(y)
    return student_id



def menu():
    print("""
          -------------MENU---------------
              1. Add a new student
              2. List all students
              3. Search students
              4. Remove a student
              5. Display single student record
              X. Exit
          """)

    menu_choice = input("Select option >  \n").upper()


    if menu_choice == '1':
        add_new_student()
    elif menu_choice == '2':
        list_all_students()
    elif menu_choice == '3':
        search_students_()
    elif menu_choice == '4':
        remove_student()
    elif menu_choice == '5':
        display_single_record()
    elif menu_choice == 'X':
        pass
    else:
        print('Invalid menu choice')
        menu()



def add_new_student():
    """
    add new student record to the data dictionary
    """
    print("-----ADD STUDENT-----")

    new_id = max(data.keys())+1
    profile_dict = {}

    profile_dict['first_name'] = input("Enter first name: \n")
    profile_dict['last_name'] = input("Enter last name:  \n")
    profile_dict['email'] = input("Enter email address:  \n")
    profile_dict['type'] = 'student'
    print("\n")

    print("Adding the following student ----------- \n")
    print(f"ID: {new_id}")
    print_student_details(profile_dict)

    data[new_id] = profile_dict

    add_option = input("Add another student... 'Y/N'").upper()
    if add_option == 'Y':
        add_new_student()
    else:
        footer_nav()


def list_all_students():
    """
    list all the student records from the data dictionary
    for each student, show the following:
    first_name, last_name, email, classes_taken, grades_received and the gpa
    """
    print("---Listing all students--- \n")
    for x, y in enumerate(data):
        profile_dict = data.get(y)
        if profile_dict.get('type') == 'student':
            print(f"ID: {y}")
            print_student_details(profile_dict)

    footer_nav()

def enter_id_to_search():
    while True:
                try:
                    student_id = int(input("Enter Student ID: "))
                    break
                except ValueError:
                    print("The input was not a valid integer.")

    return student_id

def search_students_():
    """
    search student records by student id or by email address
    """
    not_found = "Student not found"

    while True:
        print("-----SEARCH MENU-----")

        option = input("Enter 'I' to search by student id or 'E' to seach by email address: ").upper()

        if option == 'I':
            student_id = enter_id_to_search()

            if student_id in get_student_id_list():
                profile_dict = data.get(student_id)
                print_student_details(profile_dict)
                break
            else:
                print(not_found)
        elif option == 'E':
            email_to_search = input("Enter Email: ").upper()
            for x, y in enumerate(get_student_id_list()):
                profile_dict = data.get(y)
                search_students_by_email(email_to_search)
    search_option = input("Search again... 'Y/N'").upper()
    if search_option == 'Y':
        search_students_()
    else:
        footer_nav()

def search_students_by_email(email_to_search):
    email_to_search = email_to_search.upper()
    id_result_list = []
    for index, student_id in enumerate(get_student_id_list()):
        profile_dict = data.get(student_id)
        email_from_data = profile_dict.get('email').upper()
        if email_from_data == email_to_search:
            if student_id not in id_result_list:
                id_result_list.append(student_id)

    for index, value in enumerate(id_result_list):
        profile_dict = data.get(value)
        print_student_details(profile_dict)


def print_student_details(profile_dict):
    print(f"First Name:  {profile_dict.get('first_name')}")
    print(f"Last Name:  {profile_dict.get('last_name')}")
    print(f"Email:  {profile_dict.get('email')}")
    print(f"Classes Taken:  {profile_dict.get('classes_taken')}")
    print(f"Grades Received:  {profile_dict.get('grades_received')} \n")

    if profile_dict.get('grades_received') != None:
        gpa = find_grade_average(profile_dict.get('grades_received'))
        print(f"GPA: {gpa} \n")

def remove_student():
    """
    remove a student record from the data dictionary
    """
    student_id = int(input("Enter Student ID to remove: "))
    if student_id in get_student_id_list():
        profile_dict = data.get(student_id)
        print_student_details(profile_dict)
        delete_confirm = input("Remove the selected student... 'Y/N'").upper()
        if delete_confirm == 'Y':
            del data[student_id]
    else:
        print("Student not found")
    search_option = input("Search for another student to remove... 'Y/N'").upper()
    if search_option == 'Y':
        remove_student()
    else:
        footer_nav()


def display_single_record():
    """
    display a single student record by ID
    show the following:
    first name, last name, email, classes_taken, grades_received and the gpa
    """
    student_id = int(input("Enter Student ID to retrieve a record: "))
    if student_id in get_student_id_list():
        profile_dict = data.get(student_id)
        print_student_details(profile_dict)


    else:
        print("Student not found")


    search_option = input("Search again... 'Y/N'").upper()
    if search_option == 'Y':
        display_single_record()
    else:
        footer_nav()


def find_grade_average(grade_tuple):
    # below conversion based on table at:
    # https://pages.collegeboard.org/how-to-convert-gpa-4.0-scale
    grades = []
    for x, y in enumerate(grade_tuple):
        if y == 'A':
            grades.append(4)
        if y == 'B':
            grades.append(3)
        if y == 'C':
            grades.append(2)
        if y == 'D':
            grades.append(1)
        if y == 'F':
            grades.append(0)

    average = sum(grades) / len(grades)
    return "{:.2f}".format(average)


def footer_nav():
    option = input("'Y' to return to Menu, 'N' to exit program:  ").upper()

    if option == "Y":
        menu()
    elif option == "N":
        pass


def main():
    """
    function calls
    """
    admin_login()


# the driver code
if __name__ == '__main__':
    main()