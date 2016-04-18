""" calamari_7seg.py
    
    Sample program testing a seven segment display connected to a shift register (74595)
    on MinnowBoard Max + Calamari Lure running a poky image.
    [1] 74595 shift register datasheet https://www.sparkfun.com/datasheets/IC/SN74HC595.pdf
  
    How it works?
    1. Using libmraa, initialise all GPIOS:
       - Shift register clock (clk, 25)
       - Serial input (serial, 20)
       - Clear input (clr, 16)
       - Latch (latch, 18)
    2. Shift register. On every rising edge, MinnowBoard sends a bit to the shift register.
       At the end of transmision, the shift register latches the input and displays it on the 
       seven segment. 
       
    Seven segment mapping:

            f  c  dp b  a  g  e  d
    0  = 0b 0  0  1  0  0  1  0  0 = 0x24 
    1  = 0b 1  0  1  0  1  1  1  1 = 0xaf
    2  = 0b 1  1  1  0  0  0  0  0 = 0xe0
    3  = 0b 1  0  1  0  0  0  1  0 = 0xa2
    4  = 0b 0  0  1  0  1  0  1  1 = 0x2b
    5  = 0b 0  0  1  1  0  0  1  0 = 0x32
    6  = 0b 0  0  1  1  0  0  0  0 = 0x30
    7  = 0b 1  0  1  0  0  1  1  1 = 0xa7
    8  = 0b 0  0  1  0  0  0  0  0 = 0x20 
    9  = 0b 0  0  1  0  0  0  1  0 = 0x22
    A  = 0b 0  0  1  0  0  0  0  1 = 0x21
    B  = 0b 0  0  1  1  1  0  0  0 = 0x38
    C  = 0b 1  1  1  1  1  0  0  0 = 0xf8
    D  = 0b 1  0  1  0  1  0  0  0 = 0xa8
    E  = 0b 0  1  1  1  0  0  0  0 = 0x70
    F  = 0b 0  1  1  1  0  0  0  1 = 0x71
    .  = 0b 1  1  0  1  1  1  1  1 = 0xdf
"""

import mraa as m

dec_numbers = {'0':0x24,'1':0xaf,'2':0xe0,'3':0xa2,
               '4':0x2b,'5':0x32,'6':0x30,'7':0xa7,
               '8':0x20,'9':0x22,'a':0x21,'b':0x38,
               'c':0xf8,'d':0xa8,'e':0x70,'f':0x71,
               '.':0xdf,'h':0xff}

class SevenSeg(object):
    def __init__(self):
        self.clk = m.Gpio(25)
        self.serial = m.Gpio(20)
        self.latch = m.Gpio(18)
        self.clr = m.Gpio(16)

        self.clk.dir(m.DIR_OUT_LOW)
        self.latch.dir(m.DIR_OUT_LOW)
        self.serial.dir(m.DIR_OUT_LOW)
        self.clr.dir(m.DIR_OUT_LOW)

        self.halt()
    
    def write(self, str):
        self.clear_all()
        self.z = [int(a) for a in bin(dec_numbers[str])[2:]]
        for i in range (0,len(self.z)):                     
            self.serial.write(self.z[i])                    
            self.rise_fall()                                
        self.do_latch()                                         
                                                                
    def clear_all(self):                                        
        for i in range (0,3):                                   
            if i%2 == 0:                                        
                self.clr.write(1)                               
            else:                                               
                self.clr.write(0)                               
                                                                
    def rise_fall(self):                                        
        self.clk.write(1)                                       
        self.clk.write(0)                                       
                                                                
    def do_latch(self):                                         
        self.latch.write(0)      
        self.latch.write(1)                                     
        self.latch.write(0)                                     
                                                                
    def halt(self):                                             
        self.write('h')  
