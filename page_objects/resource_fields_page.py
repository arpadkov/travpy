from page_objects.page_object import PageObject


class ResourceFieldsPage(PageObject):

    def __init__(self):
        super(ResourceFieldsPage, self).__init__()

    def read_resources(self):
        lumber = self.get_element("//*[@id='l1']").text()
        clay = self.get_element("//*[@id='l2']").text()
        iron = self.get_element("//*[@id='l3']").text()
        crop = self.get_element("//*[@id='l4']").text()
        return lumber, clay, iron, crop
