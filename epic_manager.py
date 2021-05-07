from config import Config
from jira_helper import JiraHelper
from confluence_helper import ConfluenceHelper
from folder_helper import FolderHelper
import logging


class EpicManager:
    def __init__(self):
        self.logger = logging.getLogger("epic_manager_log")

        self.config = Config()
        self.config.load()

        self.jira_helper = JiraHelper(url=self.config.altassian_url, username=self.config.altassian_username,
                                      password=self.config.altassian_token,
                                      project_key=self.config.jira_project_key)

        self.confluence_helper = ConfluenceHelper(url=self.config.altassian_url,
                                                  username=self.config.altassian_username,
                                                  password=self.config.altassian_token,
                                                  space=self.config.confluence_space)

        self.folder_helper = FolderHelper(self.config.folder_target_path)

    def manage_epic(self, epic_key):
        # Do the thing
        self.logger.info(f"Looking up Epic: {epic_key}")
        result, epic = self.jira_helper.get_issue_details(issue_key=epic_key)
        epic_key = epic["key"]
        epic_summary = epic["summary"]
        self.logger.info(f"Found Epic: {epic_key}. Summary: {epic_summary}")

        # Get stories
        if self.config.folder_include_stories:
            self.logger.info(f"Looking up Stories for Epic: {epic_key}")
            result, stories = self.jira_helper.get_story_details(epic_key)
            self.logger.info(f"Got Stories")
        else:
            stories = []

        page_title = f"{epic_key}: {epic_summary}"

        self.logger.info(f"Creating confluence page: {page_title}")
        url_format = '<a href="{link}">{text}</a>'
        jira_url = url_format.format(link=f"{self.config.altassian_url}/browse/{epic_key}", text=f"{epic_key}")
        body = f"Jira link: {jira_url}"
        # result, page = self.confluence_helper.create_page(title=page_title, body=body,
        #                                                   parent_title=self.config.confluence_parent_page)
        # self.logger.info(f"Created confluence page: {page}")

        folder_name = f"{epic_key} {epic_summary}"

        self.logger.info(f"Creating Filesystem folder: {folder_name}")
        result = self.folder_helper.create_epic_folder(epic=epic, include_stories=self.config.folder_include_stories,
                                                       stories=stories)
        self.logger.info(f"Created folder: {folder_name}")

        return True
