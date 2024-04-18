from .warehouse import Warehouse
import csv
import time

class WarehouseDatabase:
    def __init__(self):
        self.warehouse_items = []

    def add_warehouse(self, item):
        self.warehouse_items.append(item)

    def check_warehouse(self, item_name):
        for item in self.warehouse_items:
            if item.item_name == item_name:
                print('This warehouse already exist')
                return True
        return False

    def edit_item(self, item_name):
        item_name = input('Enter the Warehouse name that you want to edit: ')
        for item in self.warehouse_items:
            if item.item_name == item_name:
                item.input_data()
                print ("Successfully!")
                time.sleep(1)
                return True
        print("Item Name not found")
        time.sleep(2)
        return False

    def remove_item(self, item_name):
        item_name = input('Enter the Warehouse name that you want to remove: ')
        for item in self.warehouse_items:
            if item.item_name == item_name:
                self.warehouse_items.remove(item)
                print ("Successfully!")
                time.sleep(1)
                return True
        print("Item Name not found")
        time.sleep(2)
        return False

    def show_item(self):
        print("Warehouse Database:")
        print("{:<10} {:<20} {:<20} {:<10}".format("ID", "Item Name", "Location", "Capacity"))
        for item in self.warehouse_items:
            print("{:<10} {:<20} {:<20} {:<10}".format(item.item_id, item.item_name, item.item_location, item.item_capacity))

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Item ID', 'Item Name', 'Item Location', 'Item Capacity'])
            for item in self.warehouse_items:
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