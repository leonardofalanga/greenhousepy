
class Greenhouse:
    def __init__(self):
        self.seesaw = Seesaw()

    def measure_soil_moisture(self):
        return self.seesaw.moisture_read()

