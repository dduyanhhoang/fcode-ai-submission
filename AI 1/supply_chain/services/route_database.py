from .warehouse_database import WarehouseDatabase
from ..data_structures.darray import DynamicArray
from ..data_structures.heappq import HeapPriorityQueue
from ..services.node import Node
from ..models.route import Route
import csv

inf = 10000007

class RouteDatabase:
    db = WarehouseDatabase()
    db.load_from_csv("data/warehouse_database.csv")

    def __init__(self):
        self.routes = DynamicArray()

    def add_route(self, route):
        self.routes.append(route)

    def check_route(self, origin, destination):
        for item in self.routes:
            if item.origin == origin and item.destination == destination:
                print('This route already exists')
                return True
        check_origin = check_destination = False
        for i in range(len(self.db.warehouse_items)):
            if origin == self.db.warehouse_items[i].item_name:
                check_origin = True
            if destination == self.db.warehouse_items[i].item_name:
                check_destination = True
        if not check_destination or not check_origin:
            print('Some of your warehouses does not exist')
            print('Please add a new warehouse or enter another route')
            return True
        if origin == destination:
            print('Please enter another destination')
            return True
        return False


    def edit_route(self):
        if len(self.routes) == 0:
            print("No routes available to edit.")
            return False
        
        self.show_item()  # Display available routes
        try:
            route_id = int(input("Enter the ID of the route you wish to edit: "))
            route_found = False
            for route in self.routes:
                if route.item_id == route_id:
                    route_found = True
                    try:
                        new_cost = float(input("Enter new delivery cost: "))
                        if new_cost < 0:
                            print("Cost cannot be negative. Please enter a valid cost.")
                            return False
                        route.cost = new_cost
                        print("Route cost updated successfully!")
                        return True
                    except ValueError:
                        print("Invalid cost entered. Please enter a valid number.")
                        return False
            if not route_found:
                print("Route ID not found.")
                return False
        except ValueError:
            print("Invalid input. Please enter a valid integer for the route ID.")
            return False

    def show_item(self):
        if len(self.routes) == 0:
            print("No routes available.")
            return False  # Indicating nothing to display
        print("Transportation Network:")
        print("{:<10} {:<20} {:<20} {:<10}".format("ID", "Origin", "Destination", "Cost"))
        for item in self.routes:
            print("{:<10} {:<20} {:<20} {:<10}".format(item.item_id, item.origin, item.destination, item.cost))
        return True  # Items displayed successfully

    def remove_item(self):
        if self.show_item():  # First, show items
            try:
                item_id = int(input("Enter the ID of the Route that you want to remove: "))
                for index in range(len(self.routes)):
                    route = self.routes[index]
                    if route.item_id == item_id:
                        removed = self.routes.remove(route)
                        if removed:
                            print("Route with ID {} removed successfully.".format(item_id))
                            return True
                        else:
                            print("Failed to remove route with ID {}.".format(item_id))
                            return False
                print("Route ID {} not found.".format(item_id))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        else:
            print("No routes to delete.")
        return False
    
    def apply_warehouse_edit(self, old_name, new_name):
        for item in self.routes:
            if item.origin == old_name:
                item.origin = new_name
            if item.destination == old_name:
                item.destination = new_name
    
    def apply_warehouse_remove(self, name):
        for route in self.routes[:]:
            if route.origin == name or route.destination == name:
                self.routes.remove(route)

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'From', 'To', 'Cost'])
            for item in self.routes:
                writer.writerow([item.item_id, item.origin, item.destination, item.cost])

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

    def create_graph(self):
        warehouse_names = DynamicArray()
        graph = DynamicArray()

        # Populate the warehouse_names and graph arrays
        for w in self.db.warehouse_items:
            warehouse_names.append(w.item_name)
            graph.append(Node(warehouse_names.index(w.item_name)))

        # Iterate over routes to add edges to the graph
        for route in self.routes:
            try:
                origin_idx = warehouse_names.index(route.origin)
                destination_idx = warehouse_names.index(route.destination)
                graph[origin_idx].Add_child(destination_idx, route.cost)
            except ValueError:
                # If either origin or destination warehouse name is not found, skip this route
                continue

        return graph, warehouse_names


    def find_optimal_route(self, start_name, end_name):
        graph, vertices = self.create_graph()
        if start_name not in vertices or end_name not in vertices:
            return "Invalid start or end warehouse name."
        start_idx = vertices.index(start_name)
        end_idx = vertices.index(end_name)

        dist, pred = self.run_dijkstra(graph, start_idx)
        if dist[end_idx] == inf:
            return "No path", []
        path = self.reconstruct_path(pred, start_idx, end_idx)
        path_names = [self.db.warehouse_items[idx].item_name for idx in path]

        return dist[end_idx], path_names

    def run_dijkstra(self, graph, start_idx):
        dist = DynamicArray()  # Distance from start vertex
        pred = DynamicArray()  # Predecessor in path
        for i in range(len(graph)):
            dist.append(inf)  # Initialize distances with infinity
            pred.append(-1)   # Initialize predecessors with -1

        dist[start_idx] = 0  # Set the distance to the start index to 0

        pq = HeapPriorityQueue()
        pq.add(0, start_idx)  # Use custom heap priority queue with initial vertex

        while not pq.is_empty():
            current_key, u = pq.remove_min()  # Get the vertex u with minimum dist
            if current_key > dist[u]:  # Check for outdated entry
                continue
            for child in graph[u].children:
                v = child.first
                weight = child.second
                new_dist = dist[u] + weight
                if new_dist < dist[v]:  # Relaxation step
                    dist[v] = new_dist
                    pred[v] = u
                    pq.add(new_dist, v)  # Add new distance and vertex to the heap

        return dist, pred


    def reconstruct_path(self, pred, start_idx, end_idx):
        path = DynamicArray()  # Path using DynamicArray
        at = end_idx
        while at != -1:
            path.append(at)
            at = pred[at]
        path.reverse()
        return path
