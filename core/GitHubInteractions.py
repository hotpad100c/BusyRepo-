import random
from datetime import datetime

def create_pull_request(repo, branch_name, path, content):
    pr = repo.create_pull(
        title=f"{branch_name}",
        body=(
            f"- {branch_name}\n"
            f"- {path}\n"
        ),
        head=branch_name,
        base="main"
    )
    return pr

def create_direct_commit(repo, path, content, sha):
    commit = repo.update_file(
        path,
        f"Busy update on {path} at {datetime.utcnow()} UTC",
        content,
        sha,
        branch="main"
    )
    return commit

def create_issue(repo, issue_title, issue_header, content):
    issue_body = (
        f"## {issue_header} \n\n"
        f"> {content}\n\n"
        "---\n"
    )
    issue = repo.create_issue(
        title=issue_title,
        body=issue_body,
        labels=["automation", "mutation"]
    )
    return issue
