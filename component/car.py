from abc import ABC, abstractmethod

# CLASS SERVICEABLE: implements the Serviceable interface
class Serviceable(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass

# CLASS CAR: implements the Car class, inherited from the Serviceable abstract class
class Car(Serviceable):
    def __init__(self, engine, method):
        super().__init__(engine, method)

    def needs_service(self):
        battery_needs_service = self.battery.bettery_needs_service()
        engine_needs_service = self.engine.engine_needs_service()
        return battery_needs_service or engine_needs_service

