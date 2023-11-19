
import datetime
from project import Project

def main_menu():
    """Main function for the program."""
    projects = []
    filename = "projects.txt"

    while True:
        print("\nProject Management System")
        print("(L)oad projects")
        print("(S)ave projects")
        print("(D)isplay projects")
        print("(F)ilter projects by date")
        print("(A)dd new project")
        print("(U)pdate project")
        print("(Q)uit")
        choice = input(">>> ").lower()

        if choice == "l":
            projects = load_projects(filename)
            print("Projects loaded successfully.")

        elif choice == "s":
            save_projects(projects, filename)
            print("Projects saved successfully.")

        elif choice == "d":
            if projects:
                display_projects(projects)
            else:
                print("No projects to display. Load or add new projects first.")

        elif choice == "f":
            date_str = input("Enter a date (DD/MM/YYYY) to filter projects after this date: ")
            try:
                filter_projects_by_date(projects, date_str)
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY.")


        elif choice == 'a':

            add_project(projects)

        elif choice == 'u':

            update_project(projects)

        elif choice == "q":
            print("Exiting program.")
            break

        else:
            print("Invalid choice, please try again.")

def load_projects(filename):
    """ Load projects from a file into a list of Project instances."""
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 5:  # Ensure that the line has the correct number of data points
                projects.append(Project(*parts))
    return projects

def save_projects(projects, filename):
    """ Save a list of Project objects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects(projects):
    """ Display a list of projects."""
    incomplete = sorted((p for p in projects if not p.is_complete()), key=lambda p: p.start_date)
    complete = sorted((p for p in projects if p.is_complete()), key=lambda p: p.start_date)

    print("\nIncomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("\nCompleted projects:")
    for project in complete:
        print(f"  {project}")

def filter_projects_by_date(projects, date_str):
    """ Filter and display projects that start after a specified date."""
    given_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if p.start_date > given_date]
    print("\nProjects starting after", given_date.strftime("%d/%m/%Y:"))
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(project)

def add_project(projects):
    """ Add a new Project to a list."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    percent_complete = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))


def update_project(projects):
    """ Function to update data of a project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Choose the project index to update: "))

    if project_choice < 0 or project_choice >= len(projects):
        print("Invalid project choice.")
        return

    project = projects[project_choice]

    new_percentage = input("New Percentage (leave blank for no change): ")
    new_priority = input("New Priority (leave blank for no change): ")

    new_percentage = int(new_percentage) if new_percentage else project.completion_percentage
    new_priority = int(new_priority) if new_priority else project.priority

    project.update(new_percentage, new_priority)
    print(f"Project updated: {project}")



if __name__ == "__main__":
    main_menu()
