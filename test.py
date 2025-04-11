from github import Github

# Authenticate with your GitHub token (create a token in GitHub settings)
g = Github("SHA256:I+0FgUHAnv3X2HyrSMIhSTbbUtdGMc9V8lGc+WEomME")

# Print all your repositories
for repo in g.get_user().get_repos():
    print(repo.name)
