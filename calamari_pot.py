"""calamari_pot.py

   Sample program testing the 10k pot slider connected to an ADC with SPI (MCP3004) on 
   MinnowBoard MAX + Calamari Lure running a poky image.
   [1] MCP3004 datasheet http://ww1.microchip.com/downloads/en/DeviceDoc/21295C.pdf

   How it works?
   1. Using libmraa. Initialise the SPI bus (spidev0.0, /dev/spi*) 
   frequency is set at 1Mhz (default)
   bitsPerWord 8 (default) 
   lsbmode SPI_MODE_0 (default)
   
   2. Data transmision
     
      MCP3004 Datasheet [1] http://ww1.microchip.com/downloads/en/DeviceDoc/21295C.pdf

      From the Minnowboard byte1 = 0b01 (starts communication) 
      From the MCP3004     byte1 = don't care
      From the Minnowboard byte2 = configuration byte, indicates channel to be converted (commonly 0) and selects 
                                   wether the conversion is single-ended or differential
                                   (SGL/DIFF, D2, D3, D4)
                                   See table 5-1, page 15, at [1]    
      From the MCP3004     byte2 = sends back the two most significant bits of the result (1)
      From the Minnowboard byte3 = don't care
      From the MCP3004     byte3 = sends back the result of conversion (2)
      
   3. Digital value. The MinnowBoard merges (1) and (2) to create a 10-bit 
                     digital value."""
import mraa as m
 
class Pot(object):
    def __init__(self):
        self.init = m.Spi(0) #Initialise SPI bus
        self.total_val = 0 
    def read(self):
        '''Data transmision
           (a) Starts communication
           (b) SGL/DIFF = 1, D2 = x, D3 = 0, D4 =0 --> 0b10000000 --> 0x80
           (c) Don't care
                        (a)   (b)   (c) '''
        self.b_array = [0x01, 0x80, 0x00]
        self.transfer = bytearray(self.b_array)
        self.d_transfer = self.init.write(self.transfer) #Send the set of bytes to the MCP3004
        self.total_val = (self.d_transfer[1] <<8) + self.d_transfer[2] #Merge (1) and (2) 
        self.total_val = self.total_val & 0x0003ff #Digital value from 0 to 1024
        return self.total_val
