import csv
from .route import Route

class RouteDatabase:
    def __init__(self):
        self.routes = []

    def add_route(self, route):
        self.routes.append(route)

    def check_route(self,origin,destination):
        for item in self.routes:
            # Check if already exist
            if item.origin == origin and item.destination == destination:
                print('This route already exist')
                return True

    def show_item(self):
        print("Transportation Network:")
        print("{:<10} {:<20} {:<20} {:<10}".format("ID", "Origin", "Destination", "Cost"))
        for item in self.routes:
            print("{:<10} {:<20} {:<20} {:<10}".format(item.item_id, item.origin, item.destination, item.cost))

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID','From','To','Cost'])# ...
            for route in self.routes:
                writer.writerow([route.item_id,route.origin, route.destination, route.cost])

    def load_from_csv(self, filename):
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                route = Route()
                route.origin = row['From']
                route.destination = row['To']
                route.cost = float(row['Cost'])
                route.item_id = int(row['ID'])
                self.add_route(route)