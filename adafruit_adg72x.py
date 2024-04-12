# SPDX-FileCopyrightText: Copyright (c) 2024 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_adg72x`
================================================================================

CircuitPython driver for the ADG728 and ADG729 analog matrix switches.


* Author(s): Liz Clark

Implementation Notes
--------------------

**Hardware:**

* `Adafruit ADG729 1-to-4 Analog Matrix Switch <https://www.adafruit.com/product/5932>`_"
* `Adafruit ADG728 1-to-8 Analog Matrix Switch <https://www.adafruit.com/product/5899>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

* Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
"""

import adafruit_bus_device.i2c_device as i2cdevice

try:
    import typing  # pylint: disable=unused-import
    from busio import I2C
except ImportError:
    pass

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_ADG72x.git"

ADG728_DEFAULT_ADDR = 0x4C
ADG729_DEFAULT_ADDR = 0x44

class Adafruit_ADG72x:
    """
    A driver for the ADG728/ADG729 analog multiplexers.
    """
    
    def __init__(self, i2c: typing.Type[I2C], i2c_address: int = ADG728_DEFAULT_ADDR):
        """
        Initializes the ADG72x.
        
        :param i2c: The I2C bus connected to the device.
        :type i2c: Type[I2C]
        :param i2c_address: The I2C address of the device. Defaults to 0x4C (ADG728).
        :type i2c_address: int
        """
        self.i2c_device = i2cdevice.I2CDevice(i2c, i2c_address)
    
    @property.setter
    def channels(self, bits: int):
        """
        Selects channels on the ADG72x chip based on the provided bits.
        Each bit in the 8-bit value 'bits' turns on a single channel;
        multiple channels can be enabled simultaneously.
        
        :param bits: 8-bit value representing the channels to be selected/deselected.
        :type bits: int
        """
        try:
            with self.i2c_device as i2c:
                i2c.write(bytes([bits]))
        except Exception as error:
            raise IOError("Failed to select channels on the ADG72x") from error
