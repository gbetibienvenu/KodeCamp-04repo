import os
import subprocess

# Define the users and their groups
users = [
    {"name": "Andrew", "group": "system-admins"},
    {"name": "Julius", "group": "legal"},
    {"name": "Chizi", "group": "hr-managers"},
    {"name": "Jeniffer", "group": "sales-managers"},
    {"name": "Adeola", "group": "business-strategists"},
    {"name": "Bach", "group": "ceos"},
    {"name": "Gozie", "group": "it-interns"},
    {"name": "Ogochukwu", "group": "finance-managers"}
]

# Define the directories
directories = [
    "Finance Budgets",
    "Contract Documents",
    "Business Projections",
    "Business Models",
    "Employee Data",
    "Company Vision and Mission Statement",
    "Server Configuration Script"
]

# Function to create users and groups
def create_users_and_groups():
    for user in users:
        group = user["group"]
        name = user["name"]
        try:
            # Create group if it doesn't exist
            subprocess.run(["sudo", "groupadd", "-f", group], check=True)
            # Create user and add to group
            subprocess.run(["sudo", "useradd", "-m", "-G", group, name], check=True)
            print(f"Created user {name} and added to group {group}.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create user {name} or group {group}: {e}")

# Function to create directories
def create_directories():
    base_path = "/path/to/company/documents"  # Replace with the actual base path
    if not os.path.exists(base_path):
        os.makedirs(base_path)
        
    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        try:
            os.makedirs(dir_path, exist_ok=True)
            print(f"Created directory {dir_path}.")
        except OSError as e:
            print(f"Failed to create directory {dir_path}: {e}")

# Function to create a file based on user input
def create_file():
    # Prompt user for file name and directory
    file_name = input("Enter the name of the file to create: ")
    directory_name = input("Enter the name of the directory to create the file in: ")

    # Base path for the directories
    base_path = "/path/to/company/documents"  # Replace with the actual base path

    if directory_name not in directories:
        print(f"Directory '{directory_name}' is not valid.")
        return

    # Construct the full directory path
    dir_path = os.path.join(base_path, directory_name)
    
    if not os.path.exists(dir_path):
        print(f"Directory '{directory_name}' does not exist.")
        return

    # Create the file in the specified directory
    file_path = os.path.join(dir_path, file_name)
    try:
        with open(file_path, 'w') as file:
            file.write("")  # Create an empty file
        print(f"File '{file_name}' created in directory '{directory_name}'.")
    except OSError as e:
        print(f"Failed to create file '{file_name}': {e}")

# Main function to execute the tasks
def main():
    create_users_and_groups()
    create_directories()
    create_file()

# Execute the main function
if __name__ == "__main__":
    main()

