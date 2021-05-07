from shareplum import Site
from shareplum import Office365


class SharepointHelper:
    def __init__(self, url, folder_path, username, password):
        self.folder_path = folder_path
        authcookie = Office365(url, username=username,
                               password=password).GetCookies()
        self.site = Site(site_url=url, authcookie=authcookie)

    def create_folder(self, folder_name):
        # Do some crazy folder creation
        full_path = f"{self.folder_path}/{folder_name}"
        result = self.site.Folder(full_path)
        return True, result
