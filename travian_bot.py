from page_objects.login_page import LoginPage
from page_objects.resource_fields_page import ResourceFieldsPage
from modell.build_manager import BuildManager


class TravianBot:

    def __init__(self, login_data):
        self.login_page = LoginPage(login_data)
        self.resource_fields = ResourceFieldsPage
        self.build_manager = BuildManager()

    def login(self):
        # self.resource_fields = ResourceFields(self.login_page.get_resource_fields_page())
        self.resource_fields = self.login_page.get_resource_fields_page()

    def run_resource_building(self):
        build_id = self.build_manager.select_field_to_build(
            self.resource_fields.read_resources(), self.resource_fields.read_fields()
        )
        self.resource_fields.build_field(build_id)

    def refresh_resources(self):
        self.build_manager.refresh_resources(self.resource_fields.read_resources())

    def close(self):
        self.login_page.close_browser()

    def __del__(self):
        self.login_page.close_browser()
