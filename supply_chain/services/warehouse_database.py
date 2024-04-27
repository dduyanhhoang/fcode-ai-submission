from ..data_structures.darray import DynamicArray
from ..models.warehouse import Warehouse
import csv
import time

class WarehouseDatabase:
    name_old = None
    name_new = None

    def __init__(self):
        self.warehouse_items = DynamicArray()

    def add_warehouse(self, item):
        self.warehouse_items.append(item)

    def check_warehouse(self, item_name):
        for i in range(len(self.warehouse_items)):
            if self.warehouse_items[i].item_name == item_name:
                return True
        return False

    def edit_item(self):
        self.show_item()  # Show items first to help user make the correct choice
        item_name = input('Enter the Warehouse name that you want to edit: ')
        item_found = False
        new_name = new_location = new_capacity = None
        
        for i in range(len(self.warehouse_items)):
            if self.warehouse_items[i].item_name == item_name:
                item_found = True
                while True:
                    new_name = input('Enter a new name: ')
                    if not self.check_warehouse(new_name):
                        break
                    print('This warehouse name already exists. Please try a different name.')
                new_location = input('Enter the location of your warehouse: ')
                new_capacity = input('Your warehouse capacity: ')
                self.name_old = item_name
                self.name_new = new_name
                self.warehouse_items[i].apply_edit_data(new_name, new_location, new_capacity)
                print("Warehouse successfully updated!")
                return True
        
        if not item_found:
            print("Item Name not found. Please ensure you enter the correct name as displayed above.")
            return False

    def show_item(self):
        print("Warehouse Database:")
        print("{:<10} {:<20} {:<20} {:<10}".format("ID", "Item Name", "Location", "Capacity"))
        for item in self.warehouse_items:
            print("{:<10} {:<20} {:<20} {:<10}".format(item.item_id, item.item_name, item.item_location, item.item_capacity))

    def remove_item(self, item_name):
        for i in range(len(self.warehouse_items)):
            if self.warehouse_items[i].item_name == item_name:
                removed = self.warehouse_items.remove(self.warehouse_items[i])
                if removed:
                    self.name_old = item_name
                    print("Successfully!")
                    time.sleep(1)
                    return True
        print("Item Name not found")
        time.sleep(2)
        return False
    
    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Item ID', 'Item Name', 'Item Location', 'Item Capacity'])
            for i in range(len(self.warehouse_items)):
                item = self.warehouse_items[i]
                writer.writerow([item.item_id, item.item_name, item.item_location, item.item_capacity])

    def load_from_csv(self, filename):
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                item = Warehouse(item_name=row['Item Name'])
                item.item_id = int(row['Item ID'])
                item.item_location = row['Item Location']
                item.item_capacity = float(row['Item Capacity'])
                self.add_warehouse(item)
