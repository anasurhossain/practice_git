# arena_project
#project class
class Project:
    def __init__(self, name, start_date, end_date, organization, funding, status):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.organization = organization
        self.funding = funding
        self.status = status

#Display method
    def display_details(self):

        print(f"\nProject Name: {self.name}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"Organization: {self.organization}")
        print(f"Funding: ${self.funding}")
        print(f"Status: {self.status}")

# Update project status
    def update_status(self, new_status):

        self.status = new_status


# list to store all projects
arena_projects = []

# function to search 
def search_project_by_name(name):

    for project in arena_projects:
        if project.name.lower() == name.lower():
            
            return project
    return None

# mmain menu loop
while True:
    print("\n--- ARENA Project management system ---")
    print("1. Create a new project")
    print("2. Search for a project by name")
    print("3. Update existing project status")
    print("4. Exit")
 #user input   
    choice = input("Enter your choice (1/2/3/4 or 'exit' to quit): ").strip()

    if choice.lower() in ['4', 'exit', 'x']:
        print("Exiting the program. bye!")
        break

# This is to Create a new project
    elif choice == '1':

        name = input("Enter project name: ")
        start_date = input("Enter start date (e.g., 01/02/2025): ")
        end_date = input("Enter end date (e.g., 31/01/2027): ")
        organization = input("Enter lead organization: ")
        funding = float(input("Enter funding amount (in millions): "))   #boolean
        status = input("Enter project status (e.g., Active, Completed): ")
        new_project = Project(name, start_date, end_date, organization, funding, status)
        arena_projects.append(new_project)
        print(" Project added successfully ;")

# by this i will be able to Search for a project by name
    elif choice == '2':

        search_name = input("Enter project name to search: ")
        project = search_project_by_name(search_name)
        if project:
            print("Project found:")
            project.display_details()
        else:
            print(" No project found with that name.")
