from atlassian import Jira


class JiraHelper:
    def __init__(self, url, username, password, project_key):
        self.jira = Jira(url=url, username=username, password=password)
        self.project_key = project_key

    def get_issue_summary(self, issue_key):
        # Get the issue summary with the given issue key
        result = self.jira.issue(key=issue_key)
        summary = result["fields"]["summary"]
        return True, summary
