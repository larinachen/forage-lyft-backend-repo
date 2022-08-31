from abc import ABC, abstractmethod

# CLASS ENGINEDELEGATE: implements the EngineDelegate interface
class EngineDelegate(ABC):
    def __init__(self, mileage_since_last_service):
        self.mileage_since_last_service = mileage_since_last_service

    @abstractmethod
    def engine_needs_service(self):
        pass

# CLASS CAPULETENGINE: implements the CaputletEngine class, inherited from EngineDelegate
class CapuletEngine(EngineDelegate):
    def __init__(self, mileage_since_last_service):
        super().__init__(mileage_since_last_service)

    def engine_needs_service(self):
        return self.mileage_since_last_service > 30000


# CLASS WILLOUGHBYENGINE: implements the WilloughbyEngine class, inherited from EngineDelegate
class WilloughbyEngine(EngineDelegate):
    def __init__(self, mileage_since_last_service):
        super().__init__(mileage_since_last_service)

    def engine_needs_service(self):
        return self.mileage_since_last_service > 60000      

# CLASS STERNMANENGINE: implements the SternmanEngine class, inherited from EngineDelegate
class SternmanEngine(EngineDelegate):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def engine_needs_service(self):
        return self.warning_light_on