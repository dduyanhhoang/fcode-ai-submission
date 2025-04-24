class Route:
    next_id = 1
    def __init__(self):
        self.item_id = Route.next_id
        Route.next_id += 1
        self.origin = None
        #self.origin_location = None
        self.destination = None
        #self.destination_location = None
        self.cost = None

    def __eq__(self, other):
        if isinstance(other, Route):
            return self.item_id == other.item_id
        return False

    def input_data(self):
        self.origin = input("Send from: ")
        self.destination = input("Send to: ")
        self.cost = float(input("Delivery Cost: "))

    def apply_new_cost(self):
        self.cost = float(input("Enter new delivery cost: "))
