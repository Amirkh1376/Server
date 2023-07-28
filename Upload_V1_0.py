from tkinter import filedialog
from github import Github

def select_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=(("All files", "*.*"),))

    if file_path:
        upload_file_to_github(file_path)

def upload_file_to_github(file_path):
    access_token = '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'
    repository = 'Amirkh1376/Server'
    target_branch = 'Test'
    file_name = file_path.split("/")[-1]

    with open(file_path, 'r') as file:
        content = file.read()

    g = Github(access_token)
    repo = g.get_repo(repository)

    try:
        # Check if the file already exists in the repository
        existing_file = repo.get_contents(file_name, ref=target_branch)
        # If the file exists, update its content
        repo.update_file(existing_file.path, "Update file", content, existing_file.sha, branch=target_branch)
    except:
        # If the file doesn't exist, create it
        repo.create_file(file_name, "Create file", content, branch=target_branch)

select_file()
