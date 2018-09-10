"""
.. module:: SL19

***************
 SL19 Module
***************

This is a Module for the `SL19 xChip <https://wiki.xinabox.cc/SL19_-_IR_Temperature>`_.
The board is based off the MLX90614 infrared light/radiation (IR) temperature sensor manufactured by Melexis Technologies NV.
The board uses I2C for communication.

Data Sheets:

-  `MLX90614 <https://www.melexis.com/en/product/MLX90614/Digital-Plug-Play-Infrared-Thermometer-TO-Can>`_

	"""

import i2c

MLX90614_REG_RAWIR1 = 0x04
MLX90614_REG_RAWIR2 = 0x05
MLX90614_REG_TA 	= 0x06
MLX90614_REG_TOBJ1 	= 0x07
MLX90614_REG_TOBJ2 	= 0x08
MLX90614_REG_TOMAX 	= 0x20
MLX90614_REG_TOMIN 	= 0x21
MLX90614_REG_PWMCTRL = 0x22
MLX90614_REG_TARANGE = 0x23
MLX90614_REG_EMISS 	= 0x24
MLX90614_REG_CONFIG = 0x25
MLX90614_REG_ADDR 	= 0x0E
MLX90614_REG_ID1 	= 0x3C
MLX90614_REG_ID2 	= 0x3D
MLX90614_REG_ID3 	= 0x3E
MLX90614_REG_ID4 	= 0x3F

class SL19(i2c.I2C):
	'''

===============
SL19 class
===============

.. class:: SL19(self,drvname,addr=0x5A,clk=100000)

		Create an instance of the SL19 class.

		:param drvname: I2C Bus used '( I2C0, ... )'
		:param addr: Slave address, default 0x5A
		:param clk: Clock speed, default 100kHz

	'''

	def __init__(self, drvname=I2C0, addr=0x5A, clk=100000):
		i2c.I2C.__init__(self, drvname, addr, clk)
		self._addr = addr
		try:
			self.start()
		except PeripheralError as e:
			print(e)
		
	def init(self):
		'''
.. method:: init(self)

		Empty function. Only used to conform with other modules.
		No configuartion required for MLX90614.

		'''
		return True
		
	def getAmbientTempC(self):
		'''
.. method:: getAmbientTempC(self)

		Returns the ambient temperature in degree celcius

		'''
		return self.readAmbient()
		
	def getAmbientTempF(self):
		'''
.. method:: getAmbientTempF(self)

		Returns the ambient temperature in degree fahrenheit

		'''
		return ((self.readAmbient() * 1.8) + 32)
	
	def getObjectTempC(self):
		'''
.. method:: getObjectTempC(self)

		Returns the object temperature in degree celcius

		'''

		return self.readObject()
		
	def getObjectTempF(self):
		'''
.. method:: getObjectTempF(self)

		Returns the object temperature in degree fahrenheit

		'''
		return ((self.readObject() * 1.8) + 32)
		
	def readAmbient(self):
		tempData = self.readTemp(MLX90614_REG_TA)
		tempData = tempData * 0.02
		tempData = tempData - 273.15
		ambient_temp = tempData
		return ambient_temp
		
	def readObject(self):
		tempData = self.readTemp(MLX90614_REG_TOBJ1)
		tempData = tempData * 0.02
		tempData = tempData - 273.15
		object_temp = tempData
		return object_temp
		
	def readTemp(self, reg):
		data = self.write_read(reg, 3)
		data = (data[0] + ((data[1] & 0x7F) << 8))
		return data
