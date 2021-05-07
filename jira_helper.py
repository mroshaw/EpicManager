from atlassian import Jira
import logging


class JiraHelper:
    def __init__(self, url, username, password, project_key):
        self.logger = logging.getLogger("epic_manager_log")
        self.jira = Jira(url=url, username=username, password=password)
        self.project_key = project_key

    def get_issue_details(self, issue_key):
        # Get the issue summary with the given issue key
        self.logger.info(f"Getting issue details from Jira: {issue_key}")
        result = self.jira.issue(key=issue_key)
        issue_summary = result["fields"]["summary"]
        issue = {"key": issue_key, "summary": issue_summary}
        self.logger.info(f"Issue details retrieved!")

        return True, issue

    def get_story_details(self, epic_key):
        # Get all story details from an Epic
        self.logger.info(f"Getting Story details from Jira: {epic_key}")
        jql = f"project = {self.project_key} AND 'Epic Link' = {epic_key}"
        stories = []
        result = self.jira.jql(jql)
        issues = result["issues"]
        for issue in issues:
            issue_key = issue["key"]
            issue_summary = issue["fields"]["summary"]
            issue_dict = {"key": issue_key, "summary": issue_summary}
            stories.append(issue_dict)

        self.logger.info(f"Story details retrieved!")
        return True, stories
