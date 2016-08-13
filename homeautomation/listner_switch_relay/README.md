# Control 5V coil relay with Raspberry Pi GPIO pin

Pi GPIO pins have a voltage of 3.3 V. This is much lower than the 6V needed to switch a RH SH 1060 relay module

We can ue the 3.3V as a signal voltage by giving it to the Base terminal of the trasistor

3.3V is connected to Pin 17 (or whatever pin you want to use to control the relay

For a detailed circuit diagram refer
https://www.openhomeautomation.net/control-a-relay-from-anywhere-using-the-raspberry-pi/

