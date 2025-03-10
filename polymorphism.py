    #polymorphism overriding
class Phone:
    def sound(self):
        return "ring ring"

class Landline(Phone):
    def sound(self):
        return "landline ringing"

class Mobile(Phone):
    def sound(self):
        return "mobile ringing"

# Function demonstrating polymorphism
def rings(phone: Phone):
    print(phone.sound())

landline=Landline()
mobile=Mobile()

rings(landline)
rings(mobile)

