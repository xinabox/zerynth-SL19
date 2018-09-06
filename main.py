import streams
import sl19

streams.serial()

SL19 = sl19.SL19(I2C0)
SL19.init()

while True:
    tempAmbient = SL19.getAmbientTempC()
    tempObject = SL19.getObjectTempC()
    
    print('Ambient: ',tempAmbient,' C')
    print('Object : ',tempObject,' C')
    
    sleep(2000)