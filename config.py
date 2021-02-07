import configparser
from configparser import NoSectionError, NoOptionError
import os


class Config:
    def __init__(self):
        self.folder_target_path = ""

        self.altassian_url = ""
        self.altassian_token = ""
        self.altassian_username = ""

        self.jira_project_key = ""

        self.confluence_space = ""
        self.confluence_parent_page = ""

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

            self.altassian_url = config.get("Atlassian", "url")
            self.altassian_token = config.get("Atlassian", "token")
            self.altassian_username = config.get("Atlassian", "username")

            self.jira_project_key = config.get("Jira", "project_key")

            self.confluence_space = config.get("Confluence", "space")
            self.confluence_parent_page = config.get("Confluence", "parent_page")

            # Validate config
            result, error_text = self.validate_config()

            return result, error_text
        except NoSectionError as no_section_exception:
            error_text = f"Could not open the config file\nError Description: {no_section_exception.message}."
            return False, error_text
        except NoOptionError as no_option_error:
            error_text = f"Configuration file is incorrect.\nError Description: {no_option_error.message}."
            return False, error_text

    def validate_config(self):
        result = True
        error_text = ""

        # Check for source exists
        if not os.path.exists(self.folder_target_path):
            error_text = f"Folder path does not exist. {self.source_path}"

        return result, error_text
