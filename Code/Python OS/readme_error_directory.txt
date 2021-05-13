>>> %Run test1_serial.py
Opening Serial Connection to Arduino
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/serial/serialposix.py", line 265, in open
    self.fd = os.open(self.portstr, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
NotADirectoryError: [Errno 20] Not a directory: '/dev/tty/USB0'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/pi/Desktop/xyz_control/test1_serial.py", line 17, in <module>
    ser = serial.Serial("/dev/tty/USB0",250000) #at home using big printer system it is "/dev/tty/USB0" but with actual system in lab it is /dev/tty/ACM0
  File "/usr/lib/python3/dist-packages/serial/serialutil.py", line 240, in __init__
    self.open()
  File "/usr/lib/python3/dist-packages/serial/serialposix.py", line 268, in open
    raise SerialException(msg.errno, "could not open port {}: {}".format(self._port, msg))
serial.serialutil.SerialException: [Errno 20] could not open port /dev/tty/USB0: [Errno 20] Not a directory: '/dev/tty/USB0'
>>> 
