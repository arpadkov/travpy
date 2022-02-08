from page_objects.resource_fields_page import ResourceFieldsPage


class Resources:

    def __init__(self, resources: tuple):
        self.lumber, self.clay, self.iron, self.crop = resources

    def __str__(self):
        return f'Lumber:\t{self.lumber}\nClay\t{self.clay}\nIron:\t{self.iron}\nCrop:\t{self.crop}'


class ResourceFields:

    def __init__(self, page_object: ResourceFieldsPage):
        self.page_object = page_object
        self.resources = Resources

        self.read_resources()

    def read_resources(self):
        self.resources = Resources(self.page_object.read_resources())




