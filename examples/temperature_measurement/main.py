##############################################
#   This is an example for SL19 temperature
#	sensor.

#   Ambient and Object temperature is measured 
#	and printed out on the console.
##############################################

import streams
from xinabox.sl19 import sl19

streams.serial()

# SL19 instance
SL19 = sl19.SL19(I2C0)

# configure SL19
SL19.init()

while True:
    tempAmbient = SL19.getAmbientTempC()	# returns ambient temp in degree celcius
    tempObject = SL19.getObjectTempC()		# returns object temp in degree celcius
    
    # prints on console
    print('Ambient: ',tempAmbient,' C')
    print('Object : ',tempObject,' C')
    
    sleep(2000)