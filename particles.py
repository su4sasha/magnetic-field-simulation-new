class Particle:
    def __init__(self, coords: list[int], speed: float, speed_direction: str, charge_sign: str, charge_value: float, mass: float, is_seen_on_screen: bool):
        self.particle_data = {
            "coords": coords,
            "speed": speed,
            "speed_direction": speed_direction,
            "charge_sign": charge_sign,
            "charge_value": charge_value,
            "mass": mass,
            "is_seen_on_screen": is_seen_on_screen
        }

    def return_all_data(self):
        return self.particle_data
