import configparser
from configparser import NoSectionError, NoOptionError
import os


class Config:
    def __init__(self):
        self.folder_target_path = ""
        self.folder_include_stories = False

        self.sharepoint_url = ""
        self.sharepoint_site = ""
        self.sharepoint_folder_path = ""
        self.sharepoint_include_stories = False

        self.altassian_url = ""
        self.altassian_token = ""
        self.altassian_username = ""

        self.jira_project_key = ""

        self.confluence_space = ""
        self.confluence_parent_page = ""
        self.confluence_include_stories = False

    def load(self):
        # Load and validate config

        result = True
        error_text = ""

        try:
            # Parse the config file
            config = configparser.RawConfigParser()
            config.read('config.ini')

            # File system params
            self.folder_target_path = config.get("Folder", "target_path")
            self.folder_include_stories = config.getboolean("Folder", "include_stories")

            # Sharepoint params
            self.sharepoint_url = config.get("Sharepoint", "url")
            self.sharepoint_folder_path = config.get("Sharepoint", "folder_path")
            self.sharepoint_site = config.get("Sharepoint", "site")
            self.sharepoint_include_stories = config.getboolean("Sharepoint", "include_stories")

            # Atlassian params
            self.altassian_url = config.get("Atlassian", "url")
            self.altassian_token = config.get("Atlassian", "token")
            self.altassian_username = config.get("Atlassian", "username")

            # Jira params
            self.jira_project_key = config.get("Jira", "project_key")

            # Confluence params
            self.confluence_space = config.get("Confluence", "space")
            self.confluence_parent_page = config.get("Confluence", "parent_page")
            self.confluence_include_stories = config.getboolean("Confluence", "include_stories")

            return result, error_text
        except NoSectionError as no_section_exception:
            error_text = f"Could not open the config file\nError Description: {no_section_exception.message}."
            return False, error_text
        except NoOptionError as no_option_error:
            error_text = f"Configuration file is incorrect.\nError Description: {no_option_error.message}."
            return False, error_text
