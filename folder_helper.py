import os.path
import logging
import string


class FolderHelper:
    def __init__(self, target_path):
        self.logger = logging.getLogger("epic_manager_log")
        self.target_path = target_path

    def create_folder(self, folder_path):
        # Create folder, if it doesn't exist
        if not os.path.exists(folder_path):
            self.logger.info("Path doesn't exist. Creating folder")
            os.makedirs(folder_path)
            self.logger.info("Folder created.")
        else:
            self.logger.info("Path exists. Skipping")
        return True

    def create_issue_folder(self, issue, target_path):
        issue_summary = issue["summary"]
        issue_clean = issue_summary.translate(str.maketrans('', '', string.punctuation))
        issue_path = f"{target_path}\\{issue['key']} {issue_clean}"
        self.logger.info(f"Creating folder with path: {issue_path}")
        result = self.create_folder(issue_path)
        self.logger.info("Folder processed!")
        return result, issue_path

    def create_epic_folder(self, epic, include_stories, stories):
        # Create Epic folder and subsequent Story folders, if required

        # Create Epic folder
        self.logger.info(f"Creating Epic folder...{epic['key']}")
        result, epic_path = self.create_issue_folder(epic, self.target_path)
        if result:
            self.logger.info("Epic folder processed!")
        else:
            self.logger.error("Error processing Epic folder!")
            return False

        # Create story folders, if required
        if include_stories:
            for story in stories:
                self.logger.info(f"Creating Issue folder...{story['key']}")
                result = self.create_issue_folder(story, epic_path)
                if result:
                    self.logger.info("Story folder processed!")
                else:
                    self.logger.error("Error processing Story folder!")

        return True
