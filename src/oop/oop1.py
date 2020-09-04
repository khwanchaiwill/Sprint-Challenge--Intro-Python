# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Main class
class Vehicle():
    pass

# sub class for Vehicle
class GroundVehicle(Vehicle):
    pass

# Sub class of GroundVehicle
class Car(GroundVehicle):
    pass

# Sub class of GroundVehicle
class Motorcycle(GroundVehicle):
    pass

# Sub class of Vehicle it's FlightVehicle
class FlightVehicle(Vehicle):
    pass

# Sub class of FlightVehicle
class Airplane(FlightVehicle):
    pass


class Starship(FlightVehicle):
    pass
    