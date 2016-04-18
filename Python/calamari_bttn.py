import mraa as m

class Button(object):
    def __init__(self):
        self.b1 = m.Gpio(14)
        self.b2 = m.Gpio(10)
        self.b3 = m.Gpio(12)
        self.b1.dir(m.DIR_IN)
        self.b2.dir(m.DIR_IN)
        self.b3.dir(m.DIR_IN)
    
    def bttn1(self):
        self.reading = self.b1.read()
        if self.reading is 0: print 'Button 1 is being pressed'
        else: print 'Buton 1 is not being pressed'
    def bttn2(self):
        self.reading = self.b2.read()
        if self.reading is 0: print 'Button 2 is being pressed'
        else: print 'Buton 2 is not being pressed'
    def bttn3(self):
        self.reading = self.b3.read()
        if self.reading is 0: print 'Button 3 is being pressed'
        else: print 'Buton 3 is not being pressed'
