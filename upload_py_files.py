import os
from github import Github

def upload_py_files(token, repo_name, directory_path, target_branch):
    # Create a PyGithub instance using the access token
    g = Github(token)

    # Get the repository object
    repo = g.get_repo(repo_name)

    # Get the filename of the main script
    main_script_filename = os.path.basename(__file__)

    # Iterate over files in the directory
    for filename in os.listdir(directory_path):
        if filename != main_script_filename and filename.endswith(".py"):
            file_path = os.path.join(directory_path, filename)

            # Check if the file already exists in the repository
            file_exists = False
            try:
                existing_files = repo.get_contents("", ref=target_branch)
                for existing_file in existing_files:
                    if existing_file.path.endswith(filename):
                        file_exists = True
                        break
            except:
                pass

            if file_exists:
                print(f"File '{filename}' already exists in the repository.")
            else:
                print(f"Uploading file '{filename}'...")

                # Read the contents of the file
                with open(file_path, 'r') as file:
                    file_contents = file.read()

                # Create a new file
                repo.create_file(
                    path=filename,
                    message="Add files from app",
                    content=file_contents,
                    branch=target_branch
                )
                print(f"File '{filename}' uploaded successfully.")
        elif filename != main_script_filename:
            print(f"Skipping file '{filename}'. Only .txt files are allowed.")

# Specify the access token for authentication
access_token = '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'

# Specify the repository name
repository = 'Amirkh1376/Server'

# Get the directory path where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the directory path containing the text files
directory_path = os.path.join(script_directory)

# Specify the target branch in the repository
target_branch = 'Test'

# Call the function to upload the text files
upload_py_files(access_token, repository, directory_path, target_branch)
