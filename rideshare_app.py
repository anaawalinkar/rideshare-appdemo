# rideshare_app.py

class User:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def request_ride(self):
        print(f"{self.name} is requesting a ride from {self.location}...")
        return Ride(self)


class Driver:
    def __init__(self, name, location, available=True):
        self.name = name
        self.location = location
        self.available = available

    def accept_ride(self, ride):
        if self.available:
            self.available = False
            ride.assign_driver(self)
            print(f"{self.name} has accepted the ride!")
        else:
            print(f"{self.name} is not available to accept the ride.")

    def complete_ride(self, ride):
        if ride.status == "In Progress":
            ride.complete()
            self.available = True
            print(f"{self.name} has completed the ride.")
        else:
            print("No ride to complete.")


class Ride:
    def __init__(self, user):
        self.user = user
        self.driver = None
        self.status = "Requested"

    def assign_driver(self, driver):
        self.driver = driver
        self.status = "In Progress"

    def complete(self):
        self.status = "Completed"
        print(f"The ride for {self.user.name} is now {self.status}.")


# Sample usage
if __name__ == "__main__":
    # Create users and drivers
    user1 = User("Ana", "Downtown")
    driver1 = Driver("John", "Uptown")

    # User requests a ride
    ride1 = user1.request_ride()

    # Driver accepts and completes the ride
    driver1.accept_ride(ride1)
    driver1.complete_ride(ride1)
