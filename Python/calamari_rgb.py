import mraa as m           
                           
class Rgb(object):           
    def __init__(self):      
        self.r = m.Gpio(21)  
        self.g = m.Gpio(23)  
        self.b = m.Gpio(26)  
                             
        self.r.dir(m.DIR_OUT)
        self.g.dir(m.DIR_OUT)
        self.r.dir(m.DIR_OUT)
        self.off()      
    def off(self):         
        self.r.write(0)    
        self.g.write(0)    
        self.b.write(0)     
    def on(self,led):       
        if led is 'red':    
            self.r.write(1)
            self.g.write(0) 
            self.b.write(0) 
        elif led is 'green':
            self.g.write(1)
            self.r.write(0) 
            self.b.write(0)
        elif led is 'blue': 
            self.b.write(1) 
            self.r.write(0) 
            self.g.write(0)
