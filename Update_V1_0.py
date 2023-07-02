from github import Github

def update_files(access_token, repository, target_branch):
    g = Github(access_token)
    repo = g.get_repo(repository)
    contents = repo.get_contents('', ref=target_branch)
    repository_list = []
    for content in contents:
        if content.type == 'file':
            filename = content.name
            if filename.endswith(('.py', '.txt', '.zip')):
                raw_url = content.download_url
                repository_list.append((filename, raw_url))
    return repository_list

access_token = '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'
repository = 'Amirkh1376/Server'
target_branch = 'Test'
repository_list = update_files(access_token, repository, target_branch)
# print(repository_list)
# for repositoryÙ€filename , fileURL in repository_list:
    # print(repositoryÙ€filename , fileURL)
