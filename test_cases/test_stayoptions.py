import pytest


@pytest.mark.usefixtures("setup")
class LaunchPage:

    def launch_browser(self):
        self.driver.