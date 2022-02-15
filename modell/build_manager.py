from page_objects.resource_fields_page import Field
from modell.resources import Resources


class BuildManager:

    def __init__(self):
        self.resources = Resources

    def refresh_resources(self, resources: Resources):
        self.resources = resources

    def select_lowest_resource(self):
        # TODO: refactor to use built in method of Resources object
        resource_list = self.resources.as_list()
        lowest_value = min(resource_list)
        return resource_list.index(lowest_value) + 1

    def select_lowest_field(self, fields: list[Field]):
        resource_index = self.select_lowest_resource()

        identical_fields = []
        for field in fields:
            if resource_index == field.field_type:
                identical_fields.append(field)

        lowest_level_field = min(identical_fields)
        return lowest_level_field.field_id

    def select_field_to_build(self, resources: list, fields: list[Field]):
        self.refresh_resources(resources)
        # lowest_resource_id = self.select_lowest_resource()
        field_id = self.select_lowest_field(fields)
        return field_id


