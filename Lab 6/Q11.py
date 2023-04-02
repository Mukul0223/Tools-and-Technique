# Write a program that uses a class attributes to define some defaults titles in a college. Display the name along with title and department of the college.
class College:
    # Default titles
    principal_title = "Dr."
    professor_title = "Prof."

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display_info(self):
        # Display name, title, and department
        print(f"{self.name} ({self.get_title()}) - {self.department}")

    def get_title(self):
        # Determine title based on department
        if self.department == "Administration":
            return College.principal_title
        else:
            return College.professor_title

college_admin = College("ABC College", "Administration")
college_admin.display_info()

college_cs = College("XYZ College", "Computer Science")
college_cs.display_info()
