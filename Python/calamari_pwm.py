import mraa as m

class Pwm(self):
    def __init__(self):
        self.led1 = m.Pwm(22)
        self.led2 = m.Pwm(24)
        self.led1.period_us(70)
        self.led2.period_us(70)
        self.led1.enable(True)
        self.led2.enable(True)
    def write(self, number1, number2):
        self.led1.write(number1/100.0)
        self.led2.write(number2/100.0)
    def writel1(self,number):
        self.led1.write(number/100.0)
    def writel2(self,number):
        self.led2.write(number/100.0)

