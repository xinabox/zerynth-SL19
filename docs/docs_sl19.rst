.. module:: SL19

***************
 SL19 Module
***************

This is a Module for the `SL19 xChip <https://wiki.xinabox.cc/SL19_-_IR_Temperature>`_.
The board is based off the MLX90614 infrared light/radiation (IR) temperature sensor manufactured by Melexis Technologies NV.
The board uses I2C for communication.

Data Sheets:

-  `MLX90614 <https://www.melexis.com/en/product/MLX90614/Digital-Plug-Play-Infrared-Thermometer-TO-Can>`_

        
===============
SL19 class
===============

.. class:: SL19(self,drvname,addr=0x5A,clk=100000)

                Create an instance of the SL19 class.

                :param drvname: I2C Bus used '( I2C0, ... )'
                :param addr: Slave address, default 0x5A
                :param clk: Clock speed, default 100kHz

        
.. method:: init(self)

                Empty function. Only used to conform with other modules.
                No configuartion required for MLX90614.

                
.. method:: getAmbientTempC(self)

                Returns the ambient temperature in degree celcius

                
.. method:: getAmbientTempF(self)

                Returns the ambient temperature in degree fahrenheit

                
.. method:: getObjectTempC(self)

                Returns the object temperature in degree celcius

                
.. method:: getObjectTempF(self)

                Returns the object temperature in degree fahrenheit

                
