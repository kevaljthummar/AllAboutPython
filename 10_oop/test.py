class SmartDevice:
    brand = "HomeTech"
    
    def __init__(self, name, status):
        self.device_name = name
        self.power_status = status
        self.brand = "CustomBrand"
        
    def get_status(self):
        status = "OFF"
        if self.power_status:
            status = "ON"
        return f"{self.device_name} is {status} - {self.brand}"