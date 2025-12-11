import os
import random
from datetime import datetime
from github import Github
from RandomContentGenerator import fetch_random_text, fetch_random_word
from GitHubItneractions import create_pull_request, create_direct_commit, create_issue
from file_mutations import mutate_readme, create_random_file

repo_name = os.environ["REPO"]
token = os.environ["GH_TOKEN"]
g = Github(token)
repo = g.get_repo(repo_name)

def choose_mutation():
    mutations = ['readme', 'random_file']
    mutation_type = random.choice(mutations)
    
    if mutation_type == 'readme':
        return mutate_readme(repo)
    else:
        return create_random_file(repo)

def choose_action():
    actions = ['pr', 'commit', 'issue']
    return random.choice(actions)

if __name__ == "__main__":
    action = choose_action()
    path, new_content, sha, random_content = choose_mutation()
    
    if action == 'pr':
        branch_name = f"busy-{random.randint(100000, 999999)}"
        base_sha = repo.get_branch("main").commit.sha
        repo.create_git_ref(
            ref=f"refs/heads/{branch_name}",
            sha=base_sha
        )
        
        if sha:
            repo.update_file(
                path,
                f"Busy update on {path}",
                new_content,
                sha,
                branch=branch_name
            )
        else:
            repo.create_file(
                path,
                f"Busy create {path}",
                new_content,
                branch=branch_name
            )
        
        pr = create_pull_request(repo, branch_name, path, random_content)
        print(f"Created PR #{pr.number} from branch {branch_name}")
    
    elif action == 'commit':
        if sha:
            commit = create_direct_commit(repo, path, new_content, sha)
            print(f"Direct commit: {commit['commit'].sha}")
        else:
            commit = repo.create_file(
                path,
                f"Busy create {path}",
                new_content,
                branch="main"
            )
            print(f"Created file: {path}")
    
    elif action == 'issue':
        issue_title = f"Busy Record - {datetime.utcnow().strftime('%Y-%m-%d %H:%M')}"
        issue_header = "Random Content"
        issue = create_issue(repo, issue_title, issue_header, random_content)
        print(f"Created Issue #{issue.number}")
    
    print(f"Action: {action}")
    print(f"File: {path}")
    print(f"Content preview: {random_content[:50]}...")
