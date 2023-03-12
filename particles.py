class Particle:
    def __init__(self, coords: list[int], speed, charge_sign, charge_value, is_seen_on_screen):
        self.particle_data = {
            "coords": coords,
            "speed": speed,
            "charge_sign": charge_sign,
            "charge_value": charge_value,
            "is_seen_on_screen": is_seen_on_screen
        }

    def return_all_data(self):
        return self.particle_data
