from functools import wraps

user_data = {
    "username": {
        "password": "hashed_password",
        "currently_logged_in": False,  
        "courses": {          
            "course_name": "course_grade"
        }
    }
}

current_user = None

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user is None:
            print("You need to be logged in")
            return
        return func(*args, **kwargs)
    return wrapper

class UserSession:
    def __enter__(self):
        global current_user
        return current_user

    def __exit__(self, exc_type, exc_val, exc_tb):
        global current_user
        if current_user is not None:
            current_user = None

def run_the_system():
    global current_user

    while True:
        if current_user is None:
            print("1- Register a new account")
            print("2- Log in with an existing account")
            print("3- See total number of users in the system")
            choice = input("Please select an option: ")
            
            if choice == '1':
                register_new_user()
            elif choice == '2':
                login()
            elif choice == '3':
                get_number_of_users()

            else:
                print("Invalid option")
        else:
            print("1- Register for a new course")
            print("2- Retrieve registered courses")
            print("3- Calculate average grade for courses")
            print("4- See total number of users in the system")
            print("5- Delete your account")
            print("6- Logout")
            choice = input("Please select an option: ")
            
            if choice == '1':
                add_new_user_course()
            elif choice == '2':
                get_student_courses()
            elif choice == '3':
                calculating_the_average()
            elif choice == '4':
                get_number_of_users()
            elif choice == '5':
                remove_my_account()
            elif choice == '6':
                with UserSession():
                    print("You have been logged out.")
            else:
                print("Invalid option")


def register_new_user():
    global user_data
    username = input("Enter a username: ").strip().lower()
    if username in user_data:
        print("Username already exists")
        return
    
    password = input("Enter a password (min 16 characters, at least 2 special characters and 2 digits): ")
    
    if len(password) < 16:
        print("Password must be at least 16 characters long. Please try again.")
        return
    
    specialChar = 0
    digit = 0
    
    for char in password:
        if not char.isalnum():
            specialChar += 1
        elif char.isdigit(): 
            digit += 1

    if (specialChar < 2 or 
        digit < 2 or 
        username in password):
        print("Password does not meet requirements")
        return
    
    user_data[username] = {'username': username, 'password': password, 'courses': {}}
    print("Registration successful! Welcome")


def login():
    global current_user
    username = input("Enter your username: ").strip().lower()
    password = input("Enter your password: ")
    
    if username in user_data and user_data[username]['password'] == password:
        current_user = user_data[username]
        current_user['currently_logged_in'] = True
        print(f"Welcome back, {username}!")
    else:
        print("Invalid username or password")


@login_required
def get_student_courses():
    if current_user['courses']:
        print("Your registered courses and grades:")
        for course, grade in current_user['courses'].items():
            print(f"Course: {course}, Grade: {grade}")
    else:
        print("You haven't registered for any courses yet.")



@login_required
def add_new_user_course():
    course_name = input("Enter the course name: ").strip().title()
    if course_name in current_user['courses']:
        print(f"You are already registered for the course: {course_name}")
    else:
        current_user['courses'][course_name] = 0
        print(f"Successfully registered for the course: {course_name}")


@login_required
def calculating_the_average():
    if current_user['courses']:
        average = sum(current_user['courses'].values()) / len(current_user['courses'])
        print(f"Your average grade is: {average:.2f}")
    else:
        print("No courses registered yet. Cannot calculate an average.")


def get_number_of_users():
    print(f"Total number of users in the system: {len(user_data)}")


@login_required
def remove_my_account():
    global current_user
    if current_user:
        del user_data[current_user['username']]
        print("Your account has been deleted successfully.")
        current_user = None

run_the_system()
print(user_data)