from vector3 import Vector3

class Rocket:
    # This list of Vector3 objects keeps a record of the rocket's
    # flight path so far, relative to the launch pad, as sourced from
    # the rocket's GPS module. The last element
    # in the list represents the rocket's current location.
    gps_flight_path: list[Vector3]
    
    def __init__(self) -> None:
        # Rocket is initially resting on the launch pad, so initialize
        # gps_flight_path to contain a single Vector3 object with x, y,
        # and z all equal to zero.
        self.gps_flight_path = [Vector3()]
