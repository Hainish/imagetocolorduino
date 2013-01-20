from PIL import Image

class ImageReader():
  def __init__(self, path):
    self.im = Image.open(path)
  
  def resize(self, width, height):
    self.im = self.im.resize((width,height), Image.ANTIALIAS)
    
  def load(self):
    self.pix = self.im.load()

  def getColorAt(self, x, y):
    return self.pix[x,y]
