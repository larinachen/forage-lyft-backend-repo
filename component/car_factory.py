from abc import ABC, abstractmethod
import battery, car, engine



class CarFactory(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    # creates a car of model Calliope
    def create_calliope(self, mileage_since_last_service, days_since_last_service):
        new_calliope = car.Car(engine.CapuletEngine(mileage_since_last_service), 
                                battery.SpindlerBattery(days_since_last_service))
        return new_calliope

    # creates a car of model Glissade
    def create_glissade(self, mileage_since_last_service, days_since_last_service):
        new_glissade = car.Car(engine.WilloughbyEngine(mileage_since_last_service), 
                                battery.SpindlerBattery(days_since_last_service))
        return new_glissade

    # creates a car of model Palindrome
    def create_palindrome(self, warning_light_on, days_since_last_service):
        new_palindrome = car.Car(engine.SternmanEngine(warning_light_on), 
                                battery.SpindlerBattery(days_since_last_service))
        return new_palindrome

    # creates a car of model Rorschach
    def create_calliope(self, mileage_since_last_service, days_since_last_service):
        new_rorschach = car.Car(engine.WilloughbyEngine(mileage_since_last_service), 
                                battery.NubbinBattery(days_since_last_service))
        return new_rorschach

    # creates a car of model Thovex
    def create_calliope(self, mileage_since_last_service, days_since_last_service):
        new_thovex = car.Car(engine.CapuletEngine(mileage_since_last_service), 
                                battery.NubbinBattery(days_since_last_service))
        return new_thovex