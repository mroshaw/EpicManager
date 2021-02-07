from config import Config
from jira_helper import JiraHelper
from confluence_helper import ConfluenceHelper
from folder_helper import FolderHelper
import datetime


def log(log_text):
    now = datetime.datetime.now()
    now_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{now_date_time} : {log_text}")


class EpicManager:
    def __init__(self):
        self.config = Config()
        self.config.load()

        self.jira_helper = JiraHelper(url=self.config.altassian_url, username=self.config.altassian_username,
                                      password=self.config.altassian_token,
                                      project_key=self.config.jira_project_key)

        self.confluence_helper = ConfluenceHelper(url=self.config.altassian_url,
                                                  username=self.config.altassian_username,
                                                  password=self.config.altassian_token,
                                                  space=self.config.confluence_space)

        self.folder_helper = FolderHelper(folder_path=self.config.folder_target_path)

    def manage_epic(self, epic_key):
        # Do the thing
        log(f"Looking up Epic: {epic_key}")
        result, epic_summary = self.jira_helper.get_issue_summary(issue_key=epic_key)
        log(f"Found Epic: {epic_key}. Summary: {epic_summary}")

        page_title = f"{epic_key}: {epic_summary}"

        log(f"Creating confluence page: {page_title}")
        url_format = '<a href="{link}">{text}</a>'
        jira_url = url_format.format(link=f"{self.config.altassian_url}/browse/{epic_key}", text=f"{epic_key}")
        body = f"Jira link: {jira_url}"
        result, page = self.confluence_helper.create_page(title=page_title, body=body,
                                                          parent_title=self.config.confluence_parent_page)
        log(f"Created confluence page: {page}")

        folder_name = f"{epic_key} {epic_summary}"
        folder_path = f"{folder_name}"

        log(f"Creating folder: {folder_path}")
        result, folder = self.folder_helper.create_folder(folder_path=folder_path)
        log(f"Created folder: {folder_path}")

        return True
