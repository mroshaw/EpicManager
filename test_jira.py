from jira_helper import JiraHelper
from config import Config


def main():
    # Do the thing
    config = Config()
    config.load()
    jira = JiraHelper(url=config.altassian_url, username=config.altassian_username, password=config.altassian_token,
                      project_key=config.jira_project_key)
    epic_key = "DATA-589"
    result, epic = jira.get_issue_details(issue_key=epic_key)
    epic_key = epic["key"]
    epic_summary = epic["summary"]
    print(f"Found Epic: {epic_key}. Summary: {epic_summary}")

    # Get stories
    if config.folder_include_stories:
        print(f"Looking up Stories for Epic: {epic_key}")
        result, stories = jira.get_story_details(epic_key)
        print(f"Got Stories")
    else:
        stories = []

    epic_path = f"{config.folder_target_path}//{epic['key']} - {epic['summary']}"
    print(f"Epic path: {epic_path}")

    for story in stories:
        print(f"Creating Issue folder...{story['key']}")
        story_path = f"{config.folder_target_path}\\{story['key']} - {story['summary']}"
        print(f"Story path: {story_path}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
