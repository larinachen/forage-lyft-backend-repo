from abc import ABC, abstractmethod

# CLASS BATTERYDELEGATE: implements the BatteryDelegate interface
class BatteryDelegate(ABC):
    def __init__(self, days_since_last_service):
        self.days_since_last_service = days_since_last_service

    @abstractmethod
    def battery_needs_service(self):
        pass


# CLASS NUBBINBATTERY: implements the NubbinBattery class inherited from BatteryDelegate
class NubbinBattery(BatteryDelegate):
    
    def __init__(self, days_since_last_service):
        super().__init__(days_since_last_service)

    def battery_needs_service(self):
        return self.days_since_last_service > 365*4

# CLASS SPINDLERBATTERY: implements the SplindlerBattery class inherited from BatteryDelegate
class SpindlerBattery(BatteryDelegate):
    
    def __init__(self, days_since_last_service):
        super().__init__(days_since_last_service)

    def battery_needs_service(self):
        return self.days_since_last_service > 365*2