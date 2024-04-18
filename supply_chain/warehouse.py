class Warehouse:
    """Warehouse class"""
    def __init__(self, id, location, capacity):
        self.id = id
        self.location = location
        self.capacity = capacity
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        self._location = value

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, value):
        if value < 0 or not isinstance(value, int):
            raise ValueError("Capacity must be a positive integer")
        self._capacity = value
    
    def __str__(self) -> str:
        return f"Warehouse {self.id} at {self.location} with capacity {self.capacity}"