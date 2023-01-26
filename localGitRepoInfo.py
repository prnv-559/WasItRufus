import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import git
from datetime import datetime, date


def printRepositoryInfo(git_dir):
    repo_path = git_dir
    repo = git.Repo(git_dir) # Repo object used to programmatically interact with Git repositories
    if not repo.bare: # check that the repository loaded correctly
        headcommit = repo.head.commit
        modifiedRepo = False
        withinWeek = False
        rufus = False
        activeBranchName = repo.active_branch.name
        if len(repo.untracked_files) >= 1:
            modifiedRepo = True
        today = str(date.today())
        author = str(headcommit.authored_datetime)[0:10]
        authorYear, authorMonth, authorDay = author.split('-')
        todayYear, todayMonth, todayDay = today.split('-')
        author = str('-'.join([authorMonth, authorDay, authorYear]))
        today = str('-'.join([todayMonth, todayDay, todayYear]))
        authorDate = datetime.strptime(author, "%m-%d-%Y")
        todayDate = datetime.strptime(today, "%m-%d-%Y")
        dateDifference = todayDate - authorDate
        if dateDifference.days <= 7:
            withinWeek = True
        if headcommit.author.name.lower() == "Rufus".lower():
            rufus = True
        print("active branch:", activeBranchName)
        print("local changes:", modifiedRepo)
        print("recent commits:", withinWeek)
        print("blame Rufus:", rufus)
    else:
        print('Could not load repository at ~{}.'.format(repo_path))


if __name__ == '__main__':
    git_dir = input("Enter File Path For Local Git Repository:") # type in the file path to your local git repo
    printRepositoryInfo(git_dir)