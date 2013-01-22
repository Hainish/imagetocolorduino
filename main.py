from image_reader import ImageReader
from serial_comm import SerialComm
import time
import sys

try:
  serial_interface = sys.argv[1]
  image_file = sys.argv[2]
  colorduinos_horizontal = int(sys.argv[3])
  colorduinos_vertical = int(sys.argv[4])
  colorduino_x = int(sys.argv[5])
  colorduino_y = int(sys.argv[6])
except Exception:
  if(len(sys.argv) != 7):
    print "Usage: python main.py SERIAL_INTERFACE IMAGE_FILE COLORDUINOS_HORIZONTAL COLORDUINOS_VERTICAL COLORDUINO_X COLORDUINO_Y"
    sys.exit()

im=ImageReader(sys.argv[2])
im.resize(colorduinos_horizontal*8,colorduinos_vertical*8)
im.load()

ser = SerialComm(serial_interface)
time.sleep(2)

for x in range(0,8):
  for y in range(0,8):
    rgb = im.getColorAt(colorduino_x*8 + x, colorduino_y*8 + y)
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    print "x: %i, y: %i" % (int(colorduino_x)*8+x, int(colorduino_y*8)+y)
    line = "%02X,%02X,%02X,%02X,%02X" % (y,x,r,g,b)
    ser.writeln(line)
    print line
time.sleep(7)
ser.close()


