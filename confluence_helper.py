from atlassian import Confluence


class ConfluenceHelper:
    def __init__(self, url, username, password, space):
        self.confluence = Confluence(url=url, username=username, password=password)
        self.space = space

    def create_page(self, title, body, parent_title):
        # Do some crazy page creation
        result = self.confluence.get_page_by_title(space=self.space, title=parent_title)
        parent_id = result["id"]
        result = self.confluence.create_page(space=self.space, title=title, body=body, parent_id=parent_id)
        page = result
        return True, page
