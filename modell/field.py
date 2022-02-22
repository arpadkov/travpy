from page_objects.page_object import ClickWaitWebElement


class Field:

    def __init__(self, element: ClickWaitWebElement):
        self.element = element
        self.outer_html = self.element.get_outer_html()

        self.field_id = self.read_id()
        self.field_level = self.read_level()
        self.field_type = self.read_type()

    def read_id(self):
        id_start = self.outer_html.find('buildingSlot')
        return int(self.outer_html[id_start+12: id_start+14])

    def read_level(self):
        return int(self.element.text())

    def read_type(self):
        type_start = self.outer_html.find('gid')
        return int(self.outer_html[type_start + 3:type_start + 5])

    def __gt__(self, other):
        return self.field_level > other.field_level

    def __lt__(self, other):
        return self.field_level < other.field_level

    def __eq__(self, other):
        return self.field_id == other.field_id
