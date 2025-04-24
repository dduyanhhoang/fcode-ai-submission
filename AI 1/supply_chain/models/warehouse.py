class Warehouse:
    next_id = 1
    def __init__(self, item_name=None, item_location=None, item_capacity=None):
        self.item_id = Warehouse.next_id
        Warehouse.next_id += 1
        self.item_name = item_name
        self.item_location = item_location
        self.item_capacity = item_capacity

    def input_data(self):
        self.item_name = input('Give your Warehouse a name: ')
        self.item_location = input('Enter the location of your warehouse: ')
        self.item_capacity = input('Your warehouse capacity: ')

    def apply_edit_data(self, item_name, item_location, item_capacity):
        self.item_name = item_name
        self.item_location = item_location
        self.item_capacity = item_capacity