"""
2. electric_car.py 내 Battery 클래스에 upgrade_battery()를 추가합니다.

upgrade_battery() 메소드는 배터리 크기를 확인하고, 85kWh가 아니면 85kWh로 바꾸는 역할을 합니다.
"""


"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")  
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    
    #Battery 클래스에 upgrade_battery()메소드를 추가
    def upgrade_battery(self):
        
        #배터리 업그레이드 전 배터리의 크기 확인
        print(f"Before Battery Size : {self.battery_size}kWh")
        
        #85kWh가 아니면 85kWh로 변경
        if self.battery_size != 85:
            self.battery_size = 85
        
        #배터리 업그레이드 후 배터리의 사이즈 확인
        print(f"After Battery Size : {self.battery_size}kWh")
        
class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()